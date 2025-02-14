from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_delete_empresa():
    # Criar uma empresa antes de deletar
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

    # Deletar a empresa criada
    response_delete = client.delete("/empresas/1")
    assert response_delete.status_code == 200  # Verificar que o delete foi bem-sucedido
    assert response_delete.json() == {"message": "Empresa deletada com sucesso"}

    # Verificar que a empresa não existe mais
    response_check = client.get("/empresas/1")
    assert response_check.status_code == 404  # Deve retornar 404
