from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_empresa():
    response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678000199",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "11999999999",
        },
    )
    assert response.status_code == 200  # Sucesso
    data = response.json()
    assert data["nome"] == "Empresa Teste"
    assert data["cnpj"] == "12345678000199"
