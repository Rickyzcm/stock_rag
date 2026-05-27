# src/api/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.rag.chain import FinancialRAGChain

app = FastAPI(title="StockInsight - AI Investment Advisor")

rag_chain = FinancialRAGChain()

class QueryRequest(BaseModel):
    question: str
    user_id: str = None

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: float

@app.post("/api/query")
async def query(request: QueryRequest) -> QueryResponse:
    """投资问答接口"""
    try:
        answer = rag_chain.query(request.question)
        return QueryResponse(
            answer=answer,
            sources=[],  # TODO: 提取来源
            confidence=0.85
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
