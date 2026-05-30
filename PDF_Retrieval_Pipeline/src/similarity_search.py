from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def search_query(query):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    results = db.similarity_search(
        query,
        k=3
    )

    return results