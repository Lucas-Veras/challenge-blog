# Blog Project - Writer

![Captura de tela 2024-11-10 173926](https://github.com/user-attachments/assets/4d38233c-68ff-4924-994f-4402c58d68fe)

## Overview

This web application provides a platform for users to create and manage blog posts, categories, and comments. It uses Django Rest Framework for the backend and Vue.js for the frontend.

## Architecture

### Database

![challange-blog (4)](https://github.com/user-attachments/assets/c18dbd59-cf03-4a1a-8dce-995d34850031)

The database schema consists of the following tables:

#### `user`
- `id` (INTEGER, Primary Key, Auto Increment)
- `email` (VARCHAR, Unique)
- `last_login` (DATETIME)
- `is_staff` (BOOL)
- `is_active` (BOOL)
- `is_superuser` (BOOL)
- `avatar` (VARCHAR)
- `password` (VARCHAR)
- `person_id` (INTEGER, FK for `person.id`)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

#### `person`
- `id` (INTEGER, Primary Key, Auto Increment)
- `name` (VARCHAR)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

#### `post`
- `id` (INTEGER, Primary Key, Auto Increment)
- `title` (VARCHAR)
- `content` (TEXT)
- `author_id` (INTEGER, FK for `user.id`)
- `status` (VARCHAR)
- `category_id` (INTEGER, FK for `categorie.id`)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

#### `category`
- `id` (INTEGER, Primary Key, Auto Increment)
- `name` (VARCHAR)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

#### `comment`
- `id` (INTEGER, Primary Key, Auto Increment)
- `user_id`  (INTEGER, FK for `user.id`)
- `description` (TEXT)
- `post_id` (INTEGER, FK for `post.id`)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

## API Endpoints

### Auth

- **POST /api/auth/login**: Logs into the application and returns the refresh and access tokens.
- **POST /api/auth/logout**: Logout from the application.
- **GET /api/auth/me**: Returns the logged-in use.
- **POST /api/auth/resgister**: Create a new user.
- **POST /api/auth/token/refresh**: Return a new access token.

### Posts

- **GET /api/posts**: Fetch a list of posts.
- **GET /api/posts/{id}**: Fetch a post by ID (Has to implement)
- **POST /api/posts**: Create a new post. 
- **PUT /api/posts/{id}**: Update a post by ID. (Has to implement)
- **DELETE /api/posts/{id}**: Delete a post by ID. (Has to implement)

### Categories

- **GET /api/categories**: Fetch a list of categories. (Has to implement)
- **POST /api/categories**: Create a new category. (Has to implement)
- **PUT /api/categories/{id}**: Update a category by ID. (Has to implement)
- **DELETE /api/categories/{id}**: Delete a category by ID. (Has to implement)

### Comments

- **GET /api/comments**: Fetch a list of comments. (Has to implement)
- **POST /api/comments**: Create a new comment. (Has to implement)
- **GET /api/comments/{id}**: Fetch a specific comment by ID. (Has to implement)
- **PUT /api/comments/{id}**: Update a comment by ID. (Has to implement)
- **DELETE /api/comments/{id}**: Delete a comment by ID. (Has to implement)

## Frontend

### LoginView.vue

The `LoginView.vue` component manages user authentication and includes fields for:
- **Email:** The user's email.
- **Password:** The user's password.

### RegisterView.vue

The `RegisterView.vue` component handles user registration and includes fields for:
- **Name:** The user's full name.
- **Email:** The user's email address.
- **Password:** The user's password.

### HomeView.vue

The `HomeView.vue` is a component for listing and searching posts.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Lucas-Veras/challenge-blog.git
    ```
2. **Navigate to the Backend Directory**
   ```bash
   cd .\backend
    ```
3. **Create a Python Virtual Environment**
  - For Linux/macOS:
    ```bash
     python3 -m venv venv
    ```
  - For Windows:
    ```bash
     python -m venv venv
    ```
4. **Activate the Virtual Environment**
  - For Linux/macOS:
    ```bash
     source venv/bin/activate
    ```
  - For Windows:
    ```bash
     .\venv\Scripts\activate
    ```
5. **Install Dependecies**
- For Backend (Django Rest Framework)
    ```bash
      pip install -r requirements.txt
    ```
- For Frontend (Vue.js)

    ```bash
      cd .\frontend
    ```

    ```bash
      npm install
    ```
6. **Run Migrations**
    ```bash
      python manage.py migrate
    ```
7. **Run the Development Server**
- For backend:
   ```bash
    python manage.py runserver
    ```
- For Vue.Js:
    
    ```bash
    cd .\frontend
    ```
    
    ```bash
    npm run dev
    ```
- Then visit `http://localhost:5173/` to see the home page.

## Considerações finais - Em Português

### Resiliência

Para garantir a robustez do nosso sistema e uma melhor experiência para os usuários, adotamos as seguintes práticas de tratamento de erros:

- **Tratamento de Erros:** Antes de tentar acessar os dados de uma resposta da API, verifique se a resposta foi bem-sucedida ou seja se o status code da requsição foi HTTP 200-299. Se o status não for esperado, tratamos o problema.
- **Mensagens de Erro Claras e Informativas**: Sempre que ocorre um erro, fornecemos mensagens claras e úteis, permitindo que os usuários compreendam o que deu errado e saibam exatamente o que fazer a seguir para resolver o problema ou buscar assistência.

### Performance

Para assegurar que o sistema opere de maneira eficiente, podemos adotar alguns métodos de otimização:

- **Lazy Loading de Componentes:** Em vez de carregar todos os componentes de uma vez, carregue-os de forma assíncrona (lazy loading) quando forem realmente necessários. Isso melhora o tempo de inicialização e reduz a carga inicial de dados.
- **Reduzir o Tamanho dos Bundles:** Utilize ferramentas como o Webpack para dividir os arquivos em chunks menores. Isso melhora o tempo de carregamento inicial e faz com que o código seja carregado sob demanda.

### Segurança

Para garantir a segurança dos nossos dados e APIs, podemos adotar as seguintes medidas:

- **Autenticação com Token Seguro (JWT)** Utilizamos o JSON Web Token (JWT) para autenticação de usuários. Os tokens devem ser gerados no login e enviados nas requisições subsequentes para validar a identidade do usuário.
- **Criptografia de Senhas:** As senhas dos usuários devem ser armazenadas de forma segura utilizando algoritmos de hash para evitar vazamentos em caso de acesso não autorizado ao banco de dados.
- **Monitoramento e Logging:** Implementamos registros de acesso (logs) e monitoramos as tentativas de login, para detectar comportamentos suspeitos e possíveis ataques, como tentativas de login com senhas incorretas.

### Usabilidade

As boas práticas para usabilidade do sistema são essenciais para garantir que os usuários possam interagir com a aplicação de forma eficiente, intuitiva e agradável. Algumas das principais práticas incluem:

- **Design Intuitivo/Interface limpa e simples:** Evitamos sobrecarregar o usuário com informações excessivas ou controles desnecessários. Organizamos os elementos de forma lógica e fácil de entender.
- **Feedback Claro e Imediato:** Quando o usuário cometer um erro, fornecemos mensagens que expliquem o que aconteceu e como corrigir o problema. Evitamos mensagens vagas como "Erro 404" ou "Algo deu errado".
