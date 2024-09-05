import os
from dotenv import load_dotenv
from groq import Groq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the .env file
load_dotenv()

GROQ_API = os.getenv("GROQ_API")
EMBEDDINGS = HuggingFaceEmbeddings()  # Cache embeddings to avoid loading multiple times
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# FAISS Search function
def search_with_faiss(query, college):
    index_path = f"faiss_index_{college}"
    directory_path = f"files/{college}"

    # Load FAISS index or create it if it doesn't exist
    faiss_index = _load_or_create_faiss_index(index_path, directory_path)

    # Retrieve documents based on query using FAISS index
    retriever = faiss_index.as_retriever(k=5)
    docs = retriever.invoke(query, k=5)  # Retrieve top 5 relevant documents

    # Rank the retrieved documents using semantic similarity
    ranked_docs = _rank_documents_by_similarity(query, docs)

    return ranked_docs

# Function to load or create FAISS index
def _load_or_create_faiss_index(index_path, directory_path):
    try:
        # Load FAISS index if it exists
        return FAISS.load_local(index_path, EMBEDDINGS, allow_dangerous_deserialization=True)
    except FileNotFoundError:
        print("FAISS index not found. Creating a new index.")
        # Create FAISS index by loading PDF files
        return _load_pdfs_and_create_faiss(directory_path, index_path)

# Function to load PDF files and create FAISS index
def _load_pdfs_and_create_faiss(directory_path, index_path):
    # Get all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]

    all_pages = []
    for pdf_file in pdf_files:
        file_path = os.path.join(directory_path, pdf_file)
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        all_pages.extend(pages)

    # Create and save the FAISS index
    faiss_index = FAISS.from_documents(all_pages, EMBEDDINGS)
    faiss_index.save_local(index_path)
    return faiss_index

# Rank documents based on similarity score
def _rank_documents_by_similarity(query, docs):
    query_embedding = _get_embedding(query)

    ranked_docs = []
    for doc in docs:
        doc_embedding = _get_embedding(doc.page_content)
        similarity = cosine_similarity([query_embedding], [doc_embedding])[0][0]
        ranked_docs.append((doc, similarity))

    # Sort documents based on similarity scores (higher is better)
    ranked_docs.sort(key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in ranked_docs]

# Get embeddings for text using HuggingFace model
def _get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy().flatten()

# Groq summary generation function
def generate_summary(results, query):
    client = Groq(api_key=GROQ_API)

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": f"""
                    You are a friendly and knowledgeable virtual assistant helping students and their families understand the admission process for Government colleges in Rajasthan, India.
                    Your role is to provide clear, helpful, and concise answers to their questions about the admission process, eligibility criteria, hostel facilities, scholarships, and any other relevant details.
                    You have been provided with the following context: "{results}"
                    The student or their family has asked this question: "{query}"
                    Respond with a warm and reassuring tone, offering the most accurate and relevant information to help the user feel confident in their next steps.
                    Avoid jargon or overly technical language, and always prioritize clarity.
                    If additional information might be useful, feel free to offer it without overwhelming the user.
                    Respond in an engaging and approachable manner like a human assistant.
                    Make your responses look as if you are yourself looking at websites and providing the information. Do not mention the you are being given context.
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

    # Show output in the console
    print('Sent')

    return jsonify({
        'query': query,
        'text': summary
    })

# Test route to check if server is running
@app.route('/test')
def test():
    return jsonify({'message': 'Server is running'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
