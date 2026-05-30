from src.load_pdf import load_pdf
from src.split_text import split_documents
from src.create_embeddings import create_vector_store
from src.similarity_search import search_query


PDF_PATH = "data/sample.pdf"


def main():

    print("Loading PDF...")

    documents = load_pdf(PDF_PATH)

    print("Splitting PDF...")

    chunks = split_documents(documents)

    print("Creating Embeddings & Vector Store...")

    create_vector_store(chunks)

    print("\nPDF Retrieval Pipeline Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("Ask a Question: ")

        if query.lower() == "exit":
            break

        results = search_query(query)

        print("\nTop Results:\n")

        for i, doc in enumerate(results, start=1):
            print(f"Result {i}")
            print(doc.page_content)
            print("-" * 80)


if __name__ == "__main__":
    main()