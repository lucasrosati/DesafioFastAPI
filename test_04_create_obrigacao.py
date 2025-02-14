from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_obrigacao():
    response_create_empresa = client.post(
        "/empresas/",
        json={
            "nome": "Empresa para Obrigação",
            "cnpj": "23456789000111",  
            "endereco": "Rua Obrigação, 456",
            "email": "obrigacao@empresa.com",
            "telefone": "11988887766",
        },
    )
    assert response_create_empresa.status_code == 200, response_create_empresa.json()

    empresa_id = response_create_empresa.json()["id"]
    response_create_obrigacao = client.post(
        "/obrigacoes/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": empresa_id,  
        },
    )
    assert response_create_obrigacao.status_code == 200, response_create_obrigacao.json()

    obrigacao = response_create_obrigacao.json()
    assert obrigacao["nome"] == "Obrigação Teste"
    assert obrigacao["periodicidade"] == "mensal"
    assert obrigacao["empresa_id"] == empresa_id