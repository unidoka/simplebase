from fastapi import FastAPI

from app.api.router import router
from config.rate_limiter import global_rate_limit

app = FastAPI(
    title="Main Service",
    version="1.0.0",
)

app.middleware("http")(global_rate_limit)

app.include_router(router)

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "main-service",
    }

# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyYmFlOThiYi0zNjY5LTRkMzAtYTI4OC1iNDQ1YWU5MGJkZDUiLCJleHAiOjE3ODM1MzM4MzAsInR5cGUiOiJhY2Nlc3MifQ.W145YNJdFXvE6CLOT8pBCdn_8aKRqB-noO0lTuT0gQo",
#   "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyYmFlOThiYi0zNjY5LTRkMzAtYTI4OC1iNDQ1YWU5MGJkZDUiLCJleHAiOjE3ODYxMjQ5MzAsInR5cGUiOiJyZWZyZXNoIn0.EFjiCgIiyQt0_xNrkKPhStQG58C23afqBFbmJMmJRRw",
#   "token_type": "bearer"
# }

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyYmFlOThiYi0zNjY5LTRkMzAtYTI4OC1iNDQ1YWU5MGJkZDUiLCJleHAiOjE3ODM1MzkyNTYsInR5cGUiOiJhY2Nlc3MifQ.MwhAMysTsrQAD_3wQXDH16bzJy9XeKBDw7jjELJnKlI
