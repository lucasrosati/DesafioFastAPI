from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_delete_empresa(client):
    response_check_empresa = client.get("/empresas/1")
    if response_check_empresa.status_code == 404:
        response_create = client.post(
            "/empresas/",
            json={
                "nome": "Empresa Teste para Deletar",
                "cnpj": "98765432000199",  
                "endereco": "Rua Nova, 456",
                "email": "deletar@teste.com",
                "telefone": "11988887777",
            },
        )
        assert response_create.status_code == 200, response_create.json()

    for obrigacao_id in range(1, 10):
        response_check_obrigacao = client.get(f"/obrigacoes/{obrigacao_id}")
        if response_check_obrigacao.status_code == 200:
            obrigacao = response_check_obrigacao.json()
            if obrigacao["empresa_id"] == 1: 
                response_delete_obrigacao = client.delete(f"/obrigacoes/{obrigacao_id}")
                assert response_delete_obrigacao.status_code == 200, response_delete_obrigacao.json()

    response_delete_empresa = client.delete("/empresas/1")
    assert response_delete_empresa.status_code == 200, response_delete_empresa.json()
