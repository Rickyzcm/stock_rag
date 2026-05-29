from pymilvus import connections
# 连接到 Milvus
connections.connect(
    alias="default",
    host="localhost",
    port=19530
)

print("✅ Milvus 连接成功!")

# 获取版本信息
from pymilvus import utility
print(f"Milvus 版本: {utility.get_server_version()}")