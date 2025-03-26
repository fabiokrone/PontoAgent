# app/api/api.py
from fastapi import APIRouter
from app.api.endpoints import batidas, feriados, justificativas, secretarias, servidores, importacao

api_router = APIRouter()
api_router.include_router(batidas.router, prefix="/batidas", tags=["batidas"])
api_router.include_router(feriados.router, prefix="/feriados", tags=["feriados"])
api_router.include_router(justificativas.router, prefix="/justificativas", tags=["justificativas"])
api_router.include_router(secretarias.router, prefix="/secretarias", tags=["secretarias"])
api_router.include_router(servidores.router, prefix="/servidores", tags=["servidores"])
api_router.include_router(importacao.router, prefix="/importacao", tags=["importacao"])