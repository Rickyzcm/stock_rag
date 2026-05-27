from sentence_transformers import SentenceTransformer
from pymilvus import Collection, collecctions
import pandas as pd

class FinancialVectorizer:
    """ 将金融数据转换为向量存储"""

    def __init__(self):
        # 使用开源中文向量模型
        self.model = SentenceTransformer('BAAI/bge-small-zh-v1.5')
        self.connect_milvus()
    def connect_milvus(self):
        """连接milvus数据库"""
        connections.connect("default", host="localhost", port="19530")

    def vectorize_documents(self, decuments: list[str]) -> list[list[float]]:
        """文档向量化"""
        # 处理金融领域特定的分词
        # 例如：识别“股票代码”，“基金简称”等
        embeddings = self.model.encode(decuments,show_progress_bar=True)
        return embeddings.tolist()

    def chunk_documents(self, decuments: list[str], chunk_size:300):
        """文档分块"""
        # 金融文档的分块策略：
        # - 财报按“科目”分块（资产负债表、利润表等）
        # - 新闻按“段落”分块
        # - 研究报告按“章节”分块
        chunks= []
        for doc in decuments:
            for i in range(0, len(doc), chunk_size):
                chunks.append(doc[i:i+chunk_size])
        return chunks

    def insert_to_milvus(self, collections_name: str, documents: list,embeddings: list):
        """插入向量数据库"""
        collection = Collection(collections_name)
        # 插入元数据（文档来源、日期、股票代码等）
        collection.insert([embeddings, documents])
        collection.flush()

# 初始化 milvus
# docker run -d --name milvus -p 19350 milvusdb/milvus:latest