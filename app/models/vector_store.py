import chromadb

from langchain.vectorstores import Chroma

from langchain.embeddings.openai import OPENAIEmbeddings

class VectorStore:
    def __init__(self, path):
        self.embeddings = OPENAIEmbeddings()
        self.vectorstore = Chroma(persist_directory=path, embedding_function=self.embeddings)

    def add_documents(self, documents):
        self.vectorstore.add_documents(documents)
    
    def similarity_search(self, query, k=4):
        return self.vectorstore.similarity_search(query, k=k)