from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_obrigacao(client):
    # Cria uma obrigação específica para o teste de leitura
    response_create = client.post(
        "/obrigacoes/",
        json={
            "nome": "Obrigação de Leitura",
            "periodicidade": "anual",
            "empresa_id": 1,
        },
    )
    assert response_create.status_code == 200, response_create.json()
    
    # Obtém o ID da obrigação recém-criada
    created_obrigacao = response_create.json()
    obrigacao_id = created_obrigacao["id"]

    # Lê a obrigação criada
    response_read = client.get(f"/obrigacoes/{obrigacao_id}")
    assert response_read.status_code == 200, response_read.json()

    # Valida os dados retornados
    data = response_read.json()
    assert data["nome"] == "Obrigação de Leitura"
    assert data["periodicidade"] == "anual"
    assert data["empresa_id"] == 1
