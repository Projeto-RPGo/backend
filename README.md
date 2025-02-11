# RPGgo

## Descrição do Projeto

Orientações gerais iniciais. 
Este projeto utiliza Django como framework de desenvolvimento web e Allauth para gerenciamento de autenticação.

## Requisitos

- Python 3
- pip (gerenciador de pacotes do Python)

## Configuração do Ambiente

### 1. Criar um ambiente virtual

Primeiro, crie um ambiente virtual para isolar as dependências do projeto. Abra o terminal e execute os seguintes comandos:

### Navegar até a pasta do projeto
```bash
cd RPGgo
```

### Criar o ambiente virtual
```bash
python3 -m venv venv
```

### Ativar o ambiente virtual
```bash
source venv/bin/activate
```

## 2. Instalar o Django e o allauth
```bash
pip install django
pip install django-allauth
```
## 3. Configurar e subir o projeto
#### Realizar migrações
```bash
python manage.py migrate
```

## Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

Navegue até http://127.0.0.1:8000/homepage/