from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=120,
        chunk_overlap=20
    )
    return splitter.split_documents(documents)
