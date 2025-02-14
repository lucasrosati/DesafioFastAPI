from pydantic import BaseModel, ConfigDict, EmailStr

# Base para os schemas
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
    model_config = ConfigDict(from_attributes=True)  # Substitui a configuração 'Config'

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str  # Exemplo: "mensal", "trimestral", "anual"
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)  # Substitui a configuração 'Config'
