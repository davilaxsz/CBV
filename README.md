# Sistema de Gerenciamento de Filmes

Este é um projeto Django que permite gerenciar uma lista de filmes, incluindo criar, editar, visualizar detalhes e excluir filmes.

## Rotas principais

| URL | Método | Descrição |
|-----|--------|-----------|
| `/filmes/` | GET | Lista todos os filmes cadastrados. |
| `/filmes/novo/` | GET, POST | Cria um novo filme. |
| `/filmes/<int:pk>/` | GET | Exibe detalhes de um filme específico. |
| `/filmes/<int:pk>/editar/` | GET, POST | Edita um filme existente. |
| `/filmes/<int:pk>/excluir/` | GET, POST | Deleta um filme existente. |
| `/admin/` | GET, POST | Área administrativa do Django. |

## Estrutura de templates

- `base.html`: template base com Bootstrap.
- `listar.html`: lista de filmes.
- `form.html`: formulário para criar ou editar filmes.
- `detalhe.html`: detalhes de um filme.
- `confirm_delete.html`: confirmação de exclusão.

## Prints das telas

**Lista de filmes:**  
![Lista de filmes](prints/listar.png)

**Criar/Editar filme:**  
![Formulário de filme](prints/novo.png)

**Detalhes do filme:**  
![Detalhes do filme](prints/detalhes.png)

**Confirmar exclusão:**  
![Confirmar exclusão](prints/excluir.png)

