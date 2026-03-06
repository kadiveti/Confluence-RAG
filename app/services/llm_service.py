from langchain.chat_models import ChatOpenAI
from langchain.chains import conversational_retrieval
from langchain.memory import ConversationBufferMemory
from config import Config


class LLMService:
    def __init__(self,vector_store):
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=Config.OPENAI_API_KEY
        )
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        self.chain = conversational_retrieval.ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever= vector_store.vectorstore.as_retriever(),  # This will be set later when the vector store is initialized
            memory=self.memory
        )

        def get_response(self, query):
            try:
                response = self.chain({"question": query})
                return response['answer']
            except Exception as e:
                print(f"Error in LLMService: {e}")
                return "Sorry, I couldn't process your request at the moment."