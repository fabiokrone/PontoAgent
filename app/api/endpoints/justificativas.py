# app/api/endpoints/justificativas.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.db.session import get_db
from app.models.justificativa import Justificativa
from app.schemas.justificativa import JustificativaCreate, JustificativaUpdate, JustificativaInDB

router = APIRouter()

@router.post("/", response_model=JustificativaInDB, status_code=status.HTTP_201_CREATED)
def create_justificativa(justificativa: JustificativaCreate, db: Session = Depends(get_db)):
    db_justificativa = Justificativa(**justificativa.dict())
    db.add(db_justificativa)
    db.commit()
    db.refresh(db_justificativa)
    return db_justificativa

@router.get("/", response_model=List[JustificativaInDB])
def read_justificativas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    justificativas = db.query(Justificativa).offset(skip).limit(limit).all()
    return justificativas

@router.get("/{justificativa_id}", response_model=JustificativaInDB)
def read_justificativa(justificativa_id: int, db: Session = Depends(get_db)):
    justificativa = db.query(Justificativa).filter(Justificativa.id == justificativa_id).first()
    if justificativa is None:
        raise HTTPException(status_code=404, detail="Justificativa não encontrada")
    return justificativa

@router.put("/{justificativa_id}", response_model=JustificativaInDB)
def update_justificativa(justificativa_id: int, justificativa: JustificativaUpdate, db: Session = Depends(get_db)):
    db_justificativa = db.query(Justificativa).filter(Justificativa.id == justificativa_id).first()
    if db_justificativa is None:
        raise HTTPException(status_code=404, detail="Justificativa não encontrada")
    
    update_data = justificativa.dict(exclude_unset=True)
    
    # Se estiver aprovando a justificativa, adicionar timestamp
    if update_data.get("status") == "aprovada" and db_justificativa.status != "aprovada":
        update_data["aprovado_em"] = datetime.now()
    
    for key, value in update_data.items():
        setattr(db_justificativa, key, value)
    
    db.commit()
    db.refresh(db_justificativa)
    return db_justificativa

@router.delete("/{justificativa_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_justificativa(justificativa_id: int, db: Session = Depends(get_db)):
    justificativa = db.query(Justificativa).filter(Justificativa.id == justificativa_id).first()
    if justificativa is None:
        raise HTTPException(status_code=404, detail="Justificativa não encontrada")
    
    db.delete(justificativa)
    db.commit()
    return None