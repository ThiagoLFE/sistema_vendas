# Minhas notas para desenvolvimento do projeto

## Comandos terminal para rodar o projeto

Rodar o socket (listenner das aplicações) `uv run uvicorn app.main:app --reload`
## Rotas

- POST   /auth/login
- GET    /dashboard
- GET    /products
- POST   /products
- PUT    /products/{id}
- DELETE /products/{id}

- POST   /sales
- GET    /sales/{id}

## Banco

- users
- products
- sales
- sale_items

## Passos

1. estrutura do projeto
2. rodar API
3. banco de dados
4. models
5. CRUD simples
6. autenticação
7. dashboard