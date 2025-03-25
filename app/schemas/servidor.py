# app/schemas/servidor.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr, validator

import re

def validate_cpf(cpf: str) -> str:
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if len(cpf) != 11:
        raise ValueError('CPF deve conter 11 dígitos')
    
    # Verifica se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        raise ValueError('CPF inválido')
    
    # Validação dos dígitos verificadores
    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != int(cpf[i]):
            raise ValueError('CPF inválido')
    
    return cpf

class ServidorBase(BaseModel):
    nome: constr(min_length=3, max_length=100)
    matricula: constr(min_length=5, max_length=20)
    cpf: str
    email: str
    ativo: bool = True
    secretaria_id: int

    @validator('cpf')
    def validate_cpf_format(cls, v):
        return validate_cpf(v)

class ServidorCreate(ServidorBase):
    pass

class ServidorUpdate(BaseModel):
    nome: Optional[constr(min_length=3, max_length=100)] = None
    matricula: Optional[constr(min_length=5, max_length=20)] = None
    email: Optional[str] = None
    ativo: Optional[bool] = None
    secretaria_id: Optional[int] = None

class ServidorInDB(ServidorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True