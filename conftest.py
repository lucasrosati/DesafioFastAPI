import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base
from database import get_db, DATABASE_URL
from main import app
from fastapi.testclient import TestClient

# Configuração para usar o banco já existente
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture para configurar o cliente de teste
@pytest.fixture
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Override da dependência de banco de dados no app principal
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

# Reseta o banco de dados ao final de todos os testes
@pytest.fixture(scope="session", autouse=True)
def reset_database():
    """
    Reseta o banco de dados ao final de todos os testes.
    Remove todos os dados das tabelas e reinicia os IDs.
    """
    # Confirma que o banco está conectado antes dos testes
    with engine.connect() as connection:
        connection.execute(text("SELECT 1;"))

    yield  # Aguarda todos os testes terminarem

    # Executa os comandos de limpeza após os testes
    with engine.connect() as connection:
        connection.execute(text("TRUNCATE TABLE obrigacoes_acessorias, empresas RESTART IDENTITY CASCADE;"))
