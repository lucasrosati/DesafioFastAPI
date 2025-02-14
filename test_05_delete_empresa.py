from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_delete_empresa(client):
    # Verifica se a empresa já existe
    response_check = client.get("/empresas/1")
    if response_check.status_code == 404:
        # Cria a empresa apenas se não existir
        response_create = client.post(
            "/empresas/",
            json={
                "nome": "Empresa Teste para Deletar",
                "cnpj": "98765432000199",  # CNPJ único para evitar conflito
                "endereco": "Rua Nova, 456",
                "email": "deletar@teste.com",
                "telefone": "11988887777",
            },
        )
        assert response_create.status_code == 200, response_create.json()

    # Deleta a empresa existente
    response_delete = client.delete("/empresas/1")
    assert response_delete.status_code == 200, response_delete.json()

    # Valida que a empresa foi deletada
    response_check_after = client.get("/empresas/1")
    assert response_check_after.status_code == 404