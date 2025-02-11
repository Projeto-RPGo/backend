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

## 🌱 Configuração do Ambiente

1. Criar e ativar um ambiente virtual 🖥️

  Primeiro, vamos criar um ambiente virtual para isolar as dependências do projeto. No terminal, siga os passos abaixo:

  Navegar até a pasta do projeto:
  ```sh
  cd backend
  ```

  Criar o ambiente virtual:
  ```sh
  python3 -m venv venv
  ```

  Ativar o ambiente virtual:

  - No Linux/MacOS:
    ```sh
    source venv/bin/activate
    ```
  - No Windows:
    ```sh
    venv\Scripts\activate
    ```

2. Instalar as dependências com o requirements.txt 📦
  Com o ambiente virtual ativo, instale as dependências do projeto de uma vez, utilizando o arquivo requirements.txt:
  ```sh
  pip install -r requirements.txt
  ```

3. Configuração do Banco de Dados 🔧
  Realize as migrações necessárias para configurar o banco de dados:
  ```sh
  python manage.py migrate
  ```

4. Iniciar o servidor de desenvolvimento 🚀
Agora, com tudo configurado, inicie o servidor de desenvolvimento:
  ```sh
  python manage.py runserver
  ```

5. Acessando o Projeto 🌍
  Abra o seu navegador favorito e vá para o seguinte endereço: http://127.0.0.1:8000/homepage/
