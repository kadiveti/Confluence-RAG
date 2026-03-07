# After chunking the document, We need to have a conversation with the user. We will query the vector store with the user's question and pass the retrieved chunks to OpenAI LLM for question answering.

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from app.services.upload_document import UploadDocument
from app.models.text_split import TextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from app.models.vector_store import VectorStore
from langchain_classic.chains import ConversationalRetrievalChain



# Query from the vector store and
# pass the retrieved chunks to OpenAI LLM for question answering use prompts and conversation .

class LLMService:
    def __init__(self, document):
        self.document = document
        self.vector_store = VectorStore(document)
        self.vector_store.create_vector_store()
        self.llm = OpenAI()
        self.conversational_retrieval_chain = ConversationalRetrievalChain.from_llm(self.llm, self.vector_store.vector_store)

    def ask_question(self, question):
        response = self.conversational_retrieval_chain.run(question)
        return response
