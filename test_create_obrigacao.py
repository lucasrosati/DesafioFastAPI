from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_obrigacao():
    # Criar uma empresa antes de criar a obrigação
    response_create_empresa = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678000199",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "11999999999",
        },
    )
    assert response_create_empresa.status_code == 200

    # Criar a obrigação associada
    response_create_obrigacao = client.post(
        "/obrigacoes/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": 1,
        },
    )
    assert response_create_obrigacao.status_code == 200
    data = response_create_obrigacao.json()
    assert data["nome"] == "Obrigação Teste"
    assert data["periodicidade"] == "mensal"
