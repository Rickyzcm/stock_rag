from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from src.rag.retriever import FinancialRetriever


class FinancialRAGChain:
    """RAG 链路:检索 + LLM"""

    def __init__(self):
        self.retriever = FinancialRetriever()
        self.llm = ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0.3,  # 降低温度,提高准确性
            api_key="your-api-key"
        )
        self.prompt = PromptTemplate(
            template=FINANCIAL_PROMPT_TEMPLATE,
            input_variables=["context", "question"]
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",  # 简单拼接模式
            retriever=self.retriever,
            prompt=self.prompt
        )

    def query(self, question: str) -> str:
        """提问"""
        response = self.qa_chain.run(question)
        return response