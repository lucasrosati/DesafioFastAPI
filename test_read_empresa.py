from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_empresa():
    # Criar uma empresa antes de testar
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
    assert response_create.status_code == 200  # Verificar que a empresa foi criada com sucesso

    # Buscar a empresa criada
    response = client.get("/empresas/1")
    assert response.status_code == 200  # Verificar que a empresa foi encontrada
    data = response.json()
    assert data["nome"] == "Empresa Teste"
    assert data["endereco"] == "Rua Nova, 456"
