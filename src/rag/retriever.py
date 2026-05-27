from langchain.vectorstores import Milvus
from langchain.retrievers.bm25 import BM25Retriever
from langchain.retrievers import EnsembleRetriever

class FinancialRetriever:
    """混合检索：向量检索 + 关键词检索"""

    def __init__(self):
        # 向量检索器（语义相关性）
        self.vector_retriever= self.build_vector_retriever()

        # 关键词检索器（精确匹配）
        self.bm25_retriever = self.build_bm25_retriever()

        # 融合检索器
        self.ensemble_retriever = EnsembleRetriever(
            retrievers=[self.vector_retriever, self.bm25_retriever],
            weights=[0.6,0.4] # 权重调整
        )

    def build_vector_retriever(self):
        """基于 Milvus 的向量检索"""
        from langchain.vectorstores import Milvus
        from sentence_transformers import SentenceTransformer

        embeddings = SentenceTransformer("BAAI/bge-small-zh-v1.5")
        vector_store = Milvus(embeddings, collection_name="financial_docs")
        return vector_store.as_retriever(search_kwargs={"k": 5})

    def build_bm25_retriever(self):
        """基于 BM25 的关键词检索"""
        # 预加载金融文档
        from langchain.retrievers.bm25 import BM25Retriever

        docs = self.load_documents()  # 从 DB 加载
        return BM25Retriever.from_documents(docs)

    def retrieve(self, query: str, k: int = 5):
        """混合检索"""
        results = self.ensemble_retriever.get_relevant_documents(query)
        return results[:k]