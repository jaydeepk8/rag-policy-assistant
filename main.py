from src.loader import load_documents
from src.chunking import chunk_documents
from src.vector_store import create_vector_store
from src.rag_pipeline import load_llm, answer_question
from src.prompts import PROMPT_V2


def main():
    print("Loading documents...")
    documents = load_documents()

    print("Chunking documents...")
    chunks = chunk_documents(documents)

    print("Creating vector store...")
    vector_store = create_vector_store(chunks)

    retriever = vector_store.as_retriever(search_kwargs={"k": 1})
    llm = load_llm()

    print("\nPolicy Assistant is ready!")
    print("Ask a question (type 'exit' to quit)\n")

    while True:
        question = input("> ")
        if question.lower() == "exit":
            break

        answer = answer_question(llm, retriever, PROMPT_V2, question)
        print("\nAnswer:")
        print(answer)
        print("-" * 50)


if __name__ == "__main__":
    main()
