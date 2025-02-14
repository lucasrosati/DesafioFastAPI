from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_update_obrigacao(client):
    response_check = client.get("/obrigacoes/1")
    if response_check.status_code == 404:
        client.post(
            "/obrigacoes/",
            json={
                "nome": "Obrigação Teste",
                "periodicidade": "mensal",
                "empresa_id": 1,
            },
        )

    response_update = client.put(
        "/obrigacoes/1",
        json={
            "nome": "Obrigação Atualizada",
            "periodicidade": "anual",
            "empresa_id": 1,
        },
    )
    assert response_update.status_code == 200, response_update.json()

    data = response_update.json()
    assert data["nome"] == "Obrigação Atualizada"
    assert data["periodicidade"] == "anual"
    assert data["empresa_id"] == 1
