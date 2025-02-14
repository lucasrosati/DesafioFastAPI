from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_update_empresa():
    # Criar uma empresa antes de atualizar
    response_create = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "98765432000199",
            "endereco": "Rua Nova, 456",
            "email": "empresa2@teste.com",
            "telefone": "11988887777",
        },
    )
    assert response_create.status_code == 200

    # Atualizar a empresa criada
    response_update = client.put(
        "/empresas/1",
        json={
            "nome": "Empresa Atualizada",
            "cnpj": "98765432000199",
            "endereco": "Rua Atualizada, 789",
            "email": "atualizado@empresa.com",
            "telefone": "11977776666",
        },
    )
    assert response_update.status_code == 200  # Verificar que o update foi bem-sucedido
    data = response_update.json()
    assert data["nome"] == "Empresa Atualizada"
    assert data["endereco"] == "Rua Atualizada, 789"
