import os
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

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

def search_with_faiss(query, index_path, college):
    embeddings = HuggingFaceEmbeddings()
    try:
        faiss_index = FAISS.load_local(
            index_path, embeddings, allow_dangerous_deserialization=True
        )
    except:
        # Handle the case where index does not exist
        print("FAISS index not found. Creating a new index.")
        load_pdfs_to_faiss(f"files/{college}", index_path)
        faiss_index = FAISS.load_local(
            index_path, embeddings, allow_dangerous_deserialization=True
        )

    retriever = faiss_index.as_retriever(k=5)
    docs = retriever.invoke(query, k=5)
    return docs

if __name__ == '__main__':
    college = "MNIT_Jaipur"
    query = f"scholarships in {college}"
    index_path = f"faiss_index_{college}"
    docs = search_with_faiss(query, index_path, college)
    
    for doc in docs:
        title = doc.page_content
        print(type(title))
        print(title)