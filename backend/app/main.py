from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.core.config import settings
from app.api.v1 import journal_entries

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title=settings.app_name, version="0.1.0", docs_url="/docs", openapi_url="/openapi.json")
app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["System"])
def health():
    return {"status": "ok", "service": settings.app_name}

app.include_router(journal_entries.router, prefix="/api/v1")
