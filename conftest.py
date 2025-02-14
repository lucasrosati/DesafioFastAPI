import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base
from database import get_db, DATABASE_URL
from main import app
from fastapi.testclient import TestClient

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def reset_database():
    """
    Reseta o banco de dados ao final de todos os testes.
    Remove todos os dados das tabelas e reinicia os IDs.
    """
    yield  

    with engine.connect() as connection:
        connection.execute(text("DELETE FROM obrigacoes_acessorias;"))
        connection.execute(text("DELETE FROM empresas;"))
        connection.execute(text("ALTER SEQUENCE obrigacoes_acessorias_id_seq RESTART WITH 1;"))
        connection.execute(text("ALTER SEQUENCE empresas_id_seq RESTART WITH 1;"))
        connection.commit()
