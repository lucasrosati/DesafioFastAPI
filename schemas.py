from pydantic import BaseModel, ConfigDict, EmailStr

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str  
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
