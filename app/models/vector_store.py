# Embedded the chuncked document into a vector store
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from app.services.upload_document import UploadDocument
from app.models.text_split import TextSplitter

class VectorStore:
    def __init__(self, document):
        self.document = document
        self.upload_document = UploadDocument(document)
        self.text_splitter = TextSplitter(chunk_size=100, chunk_overlap=0)
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = Chroma(collection_name="confluence_docs", embedding_function=self.embeddings)

    def create_vector_store(self):
        # Split the document into chunks
        chunks = self.upload_document.upload_and_split()
        
        # Add the chunks to the vector store
        for chunk in chunks:
            self.vector_store.add_texts([chunk])
    
    def query_vector_store(self, query):
        # Query the vector store
        results = self.vector_store.similarity_search(query)
        return results