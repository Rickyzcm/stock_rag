# 

## 创建项目
### Python3 环境 terminal 执行
```
python -m venv venv
source venv/bin/activate
```

```
# 必要依赖
pip3 install -r requirements.txt
```
## 项目结构
```
|_data_pipeline
    |_ [crawler.py](src%2Fdata_pipeline%2Fcrawler.py) 数据来源（API获取）
    |_ [vectorizer.py](src%2Fdata_pipeline%2Fvectorizer.py)向量化与知识库构建

```