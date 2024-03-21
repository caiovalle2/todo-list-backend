# Backend da Lista de Tarefas com Login por Sessão

Este é um backend simples para uma aplicação de lista de tarefas com autenticação por sessão. Aqui estão os endpoints disponíveis e os códigos de status HTTP possíveis para cada um:

## Endpoints

- **POST `/api/register`**
  - Cria um novo usuário.
  - Parâmetros:
    - `username`: O nome de usuário desejado.
    - `password`: A senha para o novo usuário.
  - Possíveis códigos de resposta:
    - `201 Created`: Usuário criado com sucesso.
    - `400 Bad Request`: Requisição inválida (por exemplo, usuário já existente).

- **POST `/api/login`**
  - Realiza o login do usuário.
  - Parâmetros:
    - `username`: O nome de usuário do usuário existente.
    - `password`: A senha do usuário.
  - Possíveis códigos de resposta:
    - `200 OK`: Login bem-sucedido.
    - `401 Unauthorized`: Credenciais inválidas.

- **GET `/api/logout`**
  - Realiza o logout do usuário atual.
  - Possíveis códigos de resposta:
    - `200 OK`: Logout bem-sucedido.
    - `401 Unauthorized`: Não autorizado (usuário não autenticado).

- **POST `/api/task/`**
  - Cria uma nova tarefa para o usuário atualmente autenticado.
  - Parâmetros:
    - `description`: A descrição da nova tarefa.
    - `deadline`: (Opcional) O prazo (deadline) da tarefa.
  - Possíveis códigos de resposta:
    - `201 Created`: Tarefa criada com sucesso.
    - `400 Bad Request`: Requisição inválida (por exemplo, descrição em falta).
    - `401 Unauthorized`: Não autorizado (usuário não autenticado).

- **GET `/api/task/`**
  - Obtém todas as tarefas do usuário atualmente autenticado.
  - Possíveis códigos de resposta:
    - `200 OK`: Requisição bem-sucedida.
    - `401 Unauthorized`: Não autorizado (usuário não autenticado).

- **PATCH `/api/task/id/`**
  - Atualiza uma tarefa existente.
  - Parâmetros (opcional):
    - `description`: A nova descrição da tarefa.
    - `deadline`: O novo prazo (deadline) da tarefa.
    - `assigned_to`: O usuário atribuído à tarefa.
    - `is_done`: Define se a tarefa está concluída (true/false).
    - `is_active`: Define se a tarefa está ativa (true/false).
  - Possíveis códigos de resposta:
    - `200 OK`: Tarefa atualizada com sucesso.
    - `401 Unauthorized`: Não autorizado (usuário não autenticado).
    - `404 Not Found`: Tarefa não encontrada.

- **DELETE `/api/task/id/`**
  - Deleta uma tarefa existente.
  - Possíveis códigos de resposta:
    - `200 OK`: Tarefa deletada com sucesso.
    - `401 Unauthorized`: Não autorizado (usuário não autenticado).
    - `404 Not Found`: Tarefa não encontrada.
