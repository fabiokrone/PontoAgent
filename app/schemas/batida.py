# app/schemas/batida.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BatidaOriginalBase(BaseModel):
    servidor_id: int
    data_hora: datetime
    tipo: str
    dispositivo: Optional[str] = None
    localizacao: Optional[str] = None
    arquivo_origem: Optional[str] = None

class BatidaOriginalCreate(BatidaOriginalBase):
    pass

class BatidaOriginalInDB(BatidaOriginalBase):
    id: int
    importado_em: datetime
    created_at: datetime

    class Config:
        orm_mode = True

class BatidaProcessadaBase(BaseModel):
    servidor_id: int
    data_hora: datetime
    tipo: str
    status: str
    batida_original_id: Optional[int] = None
    justificativa_id: Optional[int] = None
    processado_por: Optional[str] = None

class BatidaProcessadaCreate(BatidaProcessadaBase):
    pass

class BatidaProcessadaUpdate(BaseModel):
    status: Optional[str] = None
    justificativa_id: Optional[int] = None
    processado_por: Optional[str] = None

class BatidaProcessadaInDB(BatidaProcessadaBase):
    id: int
    processado_em: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True