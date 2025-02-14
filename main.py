from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
import models, schemas

app = FastAPI()

# Inicializa o banco ao rodar a aplicação
init_db()

# Dependência do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = models.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa not found")
    return db_empresa
