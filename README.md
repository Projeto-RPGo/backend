# RPGo! 🚀

O RPGo! é um projeto web desenvolvido utilizando Django como framework backend e Allauth para o gerenciamento de autenticação de usuários. Este projeto oferece uma estrutura inicial para desenvolvimento de aplicações web seguras e escaláveis.

## ⬇️ Clonando o repositório
Você pode baixar ou clonar o projeto de duas formas:

- **Usando Git**
  ```sh
  git clone git@github.com:Projeto-RPGo/backend.git
  ```

- **Usando GitHub CLI**
  ```sh
  gh repo clone Projeto-RPGo/backend
  ```

> 💡 *Ou baixe o arquivo ZIP diretamente pelo GitHub e extraia no seu computador.*

## ⚙️ Requisitos

Antes de começar, certifique-se de que você tem as seguintes ferramentas instaladas:

- [Python](https://www.python.org) 3.10 ou superior 🐍
- [pip](https://pypi.org/project/pip/) o gerenciador de pacotes do Python 💡
- [PostgreSQL](https://www.postgresql.org) banco de dados relacional 🐘

## 🌱 Configuração do Ambiente

1. **Criar o Arquivo `.env` a Partir do Arquivo `.env.template` 📝**

    Antes de iniciar o projeto, você precisa configurar as credenciais do banco de dados e outras variáveis de ambiente. Para fazer isso, siga os passos abaixo:

    Navegue até a pasta do projeto:
    ```sh
    cd backend
    ```

    Crie o arquivo `.env` com base no `.env.template`:
    ```sh
    cp .env.template .env
    ```

    Abra o arquivo `.env` e edite com as suas credenciais do banco de dados PostgreSQL e outras variáveis necessárias:
    ```sh
    nano .env
    ```

    Exemplo de conteúdo do `.env` para PostgreSQL:
    ```ini
    DB_NAME=rpgo_db
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=myuser
    DB_PASSWORD=mypassword
    ```

2. **Executar o Script de Configuração 🔧**

    Execute o script de configuração `setup.sh` para criar e ativar o ambiente virtual, instalar as dependências e configurar o banco de dados.

    Executar o script:
    ```sh
    source setup.sh
    ```

3. **Iniciar o Servidor Django 🚀**

    Agora, com tudo configurado, inicie o servidor Django:
    ```sh
    python3 manage.py runserver
    ```

4. **Acessar o Projeto 🌍**

    Abra o seu navegador favorito e vá para o seguinte endereço:

    http://127.0.0.1:8000/homepage/

## 📊 Documentação da API

A documentação da API está disponível através do *Swagger* e do *ReDoc*.

- **Swagger:** http://127.0.0.1:8000/api/schema/swagger-ui
- **ReDoc:** http://127.0.0.1:8000/api/schema/redoc
