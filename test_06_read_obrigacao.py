from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_obrigacao(client):
    response_create = client.post(
        "/obrigacoes/",
        json={
            "nome": "Obrigação de Leitura",
            "periodicidade": "anual",
            "empresa_id": 1,
        },
    )
    assert response_create.status_code == 200, response_create.json()
    
    created_obrigacao = response_create.json()
    obrigacao_id = created_obrigacao["id"]

    response_read = client.get(f"/obrigacoes/{obrigacao_id}")
    assert response_read.status_code == 200, response_read.json()

    data = response_read.json()
    assert data["nome"] == "Obrigação de Leitura"
    assert data["periodicidade"] == "anual"
    assert data["empresa_id"] == 1
