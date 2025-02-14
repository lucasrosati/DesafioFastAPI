from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_delete_empresa(client):
    # Verifica se a empresa já existe
    response_check_empresa = client.get("/empresas/1")
    if response_check_empresa.status_code == 404:
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

    # Verifica se existem obrigações associadas à empresa
    for obrigacao_id in range(1, 10):  # Substitua 10 por um número seguro para testar
        response_check_obrigacao = client.get(f"/obrigacoes/{obrigacao_id}")
        if response_check_obrigacao.status_code == 200:
            obrigacao = response_check_obrigacao.json()
            if obrigacao["empresa_id"] == 1:  # Verifica se pertence à empresa
                response_delete_obrigacao = client.delete(f"/obrigacoes/{obrigacao_id}")
                assert response_delete_obrigacao.status_code == 200, response_delete_obrigacao.json()

    # Deleta a empresa existente
    response_delete_empresa = client.delete("/empresas/1")
    assert response_delete_empresa.status_code == 200, response_delete_empresa.json()
