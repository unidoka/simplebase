from fastapi import FastAPI
from src.api.router import router

app = FastAPI(title="Main Service", version="1.0.0")

app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "main-service"}