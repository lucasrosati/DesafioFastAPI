# Desafio FastAPI

Este projeto foi desenvolvido como parte do **Desafio FastAPI**, utilizando **Python**, **FastAPI**, e **PostgreSQL**. A aplicação realiza o CRUD para entidades como **Empresas** e suas **Obrigações Acessórias**.

---

## **Requisitos**

Antes de começar, certifique-se de que você tem os seguintes requisitos instalados:

- Python 3.10 ou superior
- PostgreSQL
- pipenv (opcional para gerenciamento de dependências)

---

## **Configuração do Ambiente**

### 1. Clone o Repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd DesafioFastAPI

2. Crie um Ambiente Virtual
bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate
3. Instale as Dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Configure o Banco de Dados
Certifique-se de que o PostgreSQL esteja rodando e crie um banco de dados chamado desafio_fastapi.

Atualize o arquivo database.py com as credenciais do banco, se necessário:

python
Copiar
Editar
DATABASE_URL = "postgresql://<usuario>:<senha>@localhost/<nome_do_banco>"
5. Execute as Migrações
bash
Copiar
Editar
python main.py
Execução
Para iniciar o servidor, execute:

bash
Copiar
Editar
uvicorn main:app --reload
A aplicação estará disponível em http://127.0.0.1:8000.

Testes
Rodando os Testes Unitários
Os testes estão configurados utilizando pytest. Para rodar todos os testes:

bash
Copiar
Editar
pytest
Certifique-se de que o banco de testes está configurado corretamente e que o ambiente está limpo.

Estrutura de Diretórios
main.py: Arquivo principal com os endpoints da API.
models.py: Modelos do SQLAlchemy para o banco de dados.
schemas.py: Esquemas para validação de dados com Pydantic.
database.py: Configuração do banco de dados.
tests/: Diretório com os arquivos de testes unitários.
Funcionalidades
Empresas
Criar Empresa: POST /empresas/
Atualizar Empresa: PUT /empresas/{empresa_id}
Ler Empresa: GET /empresas/{empresa_id}
Deletar Empresa: DELETE /empresas/{empresa_id}
Obrigações Acessórias
Criar Obrigação: POST /obrigacoes/
Atualizar Obrigação: PUT /obrigacoes/{obrigacao_id}
Ler Obrigação: GET /obrigacoes/{obrigacao_id}
Deletar Obrigação: DELETE /obrigacoes/{obrigacao_id}
Swagger UI
Acesse a documentação interativa em:
http://127.0.0.1:8000/docs

Considerações
Certifique-se de resetar o banco de dados antes de rodar os testes.
O diretório __pycache__ e arquivos desnecessários estão ignorados no .gitignore.
Autor
Desenvolvido por Lucas Rosati.
Em caso de dúvidas, sinta-se à vontade para entrar em contato.