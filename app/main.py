# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api import api_router  # Importe o roteador API

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API para gestão automatizada de ponto",
    version="0.1.0",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.CORS_ORIGINS.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir o roteador de API
app.include_router(api_router, prefix=settings.API_PREFIX)

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao Sistema Automatizado de Gestão de Ponto"}