from fastapi import FastAPI

app = FastAPI(
    title="Sistema Automatizado de Gestão de Ponto",
    description="API para gestão automática de ponto",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Sistema de Gestão de Ponto funcionando!"}