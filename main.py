from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
import models
import schemas

app = FastAPI(
    title="API de Gestão de Empresas e Obrigações Acessórias",
    description="API para gerenciar empresas e obrigações fiscais, incluindo criação, leitura, atualização e exclusão de dados.",
    version="1.0.0",
)

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/empresas/", response_model=schemas.Empresa, tags=["Empresas"])
def create_empresa(
    empresa: schemas.EmpresaCreate = Body(
        examples={
            "exemplo1": {
                "summary": "Exemplo de criação de empresa",
                "value": {
                    "nome": "Empresa Teste",
                    "cnpj": "12345678000199",
                    "endereco": "Rua Teste, 123",
                    "email": "teste@empresa.com",
                    "telefone": "11999999999",
                },
            }
        }
    ),
    db: Session = Depends(get_db),
):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.cnpj == empresa.cnpj).first()
    if db_empresa:
        raise HTTPException(status_code=400, detail="Empresa com esse CNPJ já existe.")
    new_empresa = models.Empresa(**empresa.model_dump())
    db.add(new_empresa)
    db.commit()
    db.refresh(new_empresa)
    return new_empresa

@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa, tags=["Empresas"])
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")
    return db_empresa

@app.put("/empresas/{empresa_id}", response_model=schemas.Empresa, tags=["Empresas"])
def update_empresa(
    empresa_id: int,
    empresa: schemas.EmpresaCreate = Body(
        examples={
            "exemplo1": {
                "summary": "Exemplo de atualização de empresa",
                "value": {
                    "nome": "Empresa Atualizada",
                    "cnpj": "12345678000199",
                    "endereco": "Rua Nova, 456",
                    "email": "atualizado@empresa.com",
                    "telefone": "11988887777",
                },
            }
        }
    ),
    db: Session = Depends(get_db),
):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")
    for key, value in empresa.model_dump().items():
        setattr(db_empresa, key, value)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.delete("/empresas/{empresa_id}", tags=["Empresas"])
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")
    db.delete(db_empresa)
    db.commit()
    return {"message": "Empresa deletada com sucesso"}

@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoria, tags=["Obrigações Acessórias"])
def create_obrigacao(
    obrigacao: schemas.ObrigacaoAcessoriaCreate = Body(
        examples={
            "exemplo1": {
                "summary": "Exemplo de criação de obrigação acessória",
                "value": {
                    "nome": "Obrigação Teste",
                    "periodicidade": "mensal",
                    "empresa_id": 1,
                },
            }
        }
    ),
    db: Session = Depends(get_db),
):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == obrigacao.empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa associada não encontrada.")
    new_obrigacao = models.ObrigacaoAcessoria(**obrigacao.model_dump())
    db.add(new_obrigacao)
    db.commit()
    db.refresh(new_obrigacao)
    return new_obrigacao

@app.get("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria, tags=["Obrigações Acessórias"])
def read_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada.")
    return db_obrigacao

@app.put("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria, tags=["Obrigações Acessórias"])
def update_obrigacao(
    obrigacao_id: int,
    obrigacao: schemas.ObrigacaoAcessoriaCreate = Body(
        examples={
            "exemplo1": {
                "summary": "Exemplo de atualização de obrigação acessória",
                "value": {
                    "nome": "Obrigação Atualizada",
                    "periodicidade": "anual",
                    "empresa_id": 1,
                },
            }
        }
    ),
    db: Session = Depends(get_db),
):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada.")
    for key, value in obrigacao.model_dump().items():
        setattr(db_obrigacao, key, value)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.delete("/obrigacoes/{obrigacao_id}", tags=["Obrigações Acessórias"])
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada.")
    db.delete(db_obrigacao)
    db.commit()
    return {"message": "Obrigação deletada com sucesso"}
