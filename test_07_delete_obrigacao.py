from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_delete_obrigacao(client):
    # Verifica se a obrigação já existe
    response_check = client.get("/obrigacoes/1")
    if response_check.status_code == 404:
        # Cria a obrigação apenas se não existir
        client.post(
            "/obrigacoes/",
            json={
                "nome": "Obrigação Teste",
                "periodicidade": "mensal",
                "empresa_id": 1,
            },
        )

    # Deleta a obrigação existente
    response_delete = client.delete("/obrigacoes/1")
    assert response_delete.status_code == 200, response_delete.json()

    # Verifica se a obrigação foi realmente deletada
    response_check_again = client.get("/obrigacoes/1")
    assert response_check_again.status_code == 404
