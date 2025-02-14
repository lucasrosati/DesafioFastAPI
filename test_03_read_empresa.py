from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_empresa(client):
    # Cria uma empresa antes de testar leitura
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
    assert response_create.status_code == 200, response_create.json()

    # Extrai o ID da empresa criada
    created_data = response_create.json()
    empresa_id = created_data["id"]

    # Realiza a leitura da empresa
    response_read = client.get(f"/empresas/{empresa_id}")
    assert response_read.status_code == 200, response_read.json()

    # Valida os dados retornados
    data = response_read.json()
    assert data["nome"] == "Empresa Teste"
    assert data["cnpj"] == "98765432000199"
    assert data["endereco"] == "Rua Nova, 456"
    assert data["email"] == "empresa2@teste.com"
    assert data["telefone"] == "11988887777"
