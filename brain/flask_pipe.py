import os
from dotenv import load_dotenv
from groq import Groq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from flask import Flask, request, jsonify
import json
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)


# Load the .env file
load_dotenv()

GROQ_API = os.getenv("GROQ_API")

# FAISS Search function (from faiss_db2.py)
def search_with_faiss(query, college):
    index_path=f"faiss_index_{college}"
    directory_path=f"files/{college}"
    embeddings = HuggingFaceEmbeddings()
    
    try:
        faiss_index = FAISS.load_local(
            index_path, embeddings, allow_dangerous_deserialization=True
        )
    except FileNotFoundError:
        # If FAISS index does not exist, load PDF files and create a new FAISS index
        print("FAISS index not found. Creating a new index.")
        load_pdfs_to_faiss(directory_path, index_path)
        faiss_index = FAISS.load_local(
            index_path, embeddings, allow_dangerous_deserialization=True
        )
    
    retriever = faiss_index.as_retriever(k=5)
    docs = retriever.invoke(query, k=5)  # Retrieve top 5 relevant documents
    return docs

# Function to load PDF files and create FAISS index
def load_pdfs_to_faiss(directory_path, index_path):
    embeddings = HuggingFaceEmbeddings()
    
    # Get a list of all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
    
    all_pages = []
    for pdf_file in pdf_files:
        file_path = os.path.join(directory_path, pdf_file)
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        all_pages.extend(pages)
    
    # Create and save the FAISS index
    faiss_index = FAISS.from_documents(all_pages, embeddings)
    faiss_index.save_local(index_path)

# Groq summary generation function
def generate_summary(results, query):
    client = Groq(api_key=GROQ_API)
    
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": f"""
                    You are a virtual assistant for students wishing to get into Government colleges of Rajasthan, India.
                    Your task is to answer the students' / parents or guardians' queries regarding the admission process, eligibility criteria, and other details about hostels, scholarships, and other facilities.
                    Along with the query, you're provided with the following context: "{results}"
                    You have been asked the following question: "{query}"
                    Be factually correct and provide the most relevant information to the user. 
                """
            },
        ],
        temperature=0.2,
        max_tokens=1900,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content

# Flask route for handling search queries
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query')
    college = data.get('college', 'MNIT_Jaipur')  # Default to MNIT Jaipur if not provided
    
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    
    # Step 1: Search relevant documents using FAISS
    docs = search_with_faiss(query, college)
    
    # Combine the content of the retrieved documents
    results = "\n\n".join([doc.page_content for doc in docs])
    
    # Step 2: Generate a summary using Groq
    summary = generate_summary(results, query)
    
    # Return the result as JSON
    save_results = jsonify({
        'query': query
    })

    # Append the results to a file a json file
    # with open('results.json', 'a') as f:
    #     f.write(json.dumps(save_results) + '\n')

    # show output in the console
    print('Sent')

    return jsonify({
        'text': summary
    })

@app.route('/test')
def test():
    return jsonify({'message': 'Server is running'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
