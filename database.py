from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from models import Base  # Importando o Base diretamente de models

# Carregar variáveis de ambiente
load_dotenv()

# URL do banco de dados a partir do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inicializar o banco de dados (criar tabelas)
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependência para injeção de sessão no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
