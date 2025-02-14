from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_update_empresa(client):
    response_check = client.get("/empresas/1")
    if response_check.status_code == 404:
        response_create = client.post(
            "/empresas/",
            json={
                "nome": "Empresa Teste",
                "cnpj": "12345678000199", 
                "endereco": "Rua Nova, 456",
                "email": "empresa2@teste.com",
                "telefone": "11988887777",
            },
        )
        assert response_create.status_code == 200, response_create.json()

    response_update = client.put(
        "/empresas/1",
        json={
            "nome": "Empresa Atualizada",
            "cnpj": "12345678000199",  
            "endereco": "Avenida Atualizada, 789",
            "email": "atualizado@empresa.com",
            "telefone": "11977776666",
        },
    )
    assert response_update.status_code == 200, response_update.json()

    data = response_update.json()
    assert data["nome"] == "Empresa Atualizada"
    assert data["endereco"] == "Avenida Atualizada, 789"
    assert data["email"] == "atualizado@empresa.com"
    assert data["telefone"] == "11977776666"