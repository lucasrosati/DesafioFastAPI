import pytest
from database import engine
from models import Base

@pytest.fixture(autouse=True)
def clear_db():
    # Limpar todas as tabelas antes de cada teste
    with engine.connect() as connection:
        connection.execute("TRUNCATE TABLE obrigacoes_acessorias, empresas RESTART IDENTITY CASCADE;")
        connection.commit()
