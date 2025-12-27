import os
from langchain_community.document_loaders import TextLoader


def load_documents(data_path="data"):
    documents = []

    for file_name in os.listdir(data_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(data_path, file_name)
            loader = TextLoader(file_path, encoding="utf-8")
            documents.extend(loader.load())

    return documents
