# app/schemas/justificativa.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class JustificativaBase(BaseModel):
    servidor_id: int
    data: date
    tipo: str
    descricao: str
    anexo_url: Optional[str] = None
    canal_origem: str

class JustificativaCreate(JustificativaBase):
    status: str = "pendente"

class JustificativaUpdate(BaseModel):
    tipo: Optional[str] = None
    descricao: Optional[str] = None
    anexo_url: Optional[str] = None
    status: Optional[str] = None
    aprovado_por: Optional[str] = None
    aprovado_em: Optional[datetime] = None

class JustificativaInDB(JustificativaBase):
    id: int
    status: str
    criado_em: datetime
    aprovado_por: Optional[str] = None
    aprovado_em: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True