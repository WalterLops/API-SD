# API-SD

```markdown
# Seu Projeto Django

Este é um projeto Django incrível que faz coisas incríveis. Siga as instruções abaixo para configurar e executar o projeto em seu ambiente local.

## Pré-requisitos

- Python 3.x (recomendamos o uso do Python 3.6+)
- pip (gerenciador de pacotes do Python)

## Configurando o Ambiente Virtual

1. Abra um terminal na pasta raiz do projeto.

2. Crie um ambiente virtual usando o comando Python. Substitua `nome_do_ambiente` pelo nome que você deseja dar ao seu ambiente virtual.

   ```bash
   python -m venv nome_do_ambiente
   ```

3. Ative o ambiente virtual. As instruções variam dependendo do sistema operacional:

   - **No Windows:**

     ```bash
     nome_do_ambiente\Scripts\activate
     ```

   - **No macOS e Linux:**

     ```bash
     source nome_do_ambiente/bin/activate
     ```

## Instalando as Dependências

Com o ambiente virtual ativado, você pode instalar as dependências do projeto.

1. Certifique-se de estar na pasta raiz do projeto, onde está localizado o arquivo `requirements.txt`.

2. Execute o seguinte comando para instalar as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Configurando o Banco de Dados

Antes de rodar o servidor, você precisa configurar o banco de dados, aplicar migrações e criar um superusuário (caso aplicável).

1. Acesse a pasta do projeto onde está localizado o arquivo `manage.py`.

2. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

3. (Opcional) Crie um superusuário para acessar a área administrativa:

   ```bash
   python manage.py createsuperuser
   ```

   Siga as instruções para definir um nome de usuário, endereço de e-mail e senha para o superusuário.

## Rodando o Servidor

Agora que tudo está configurado, você pode iniciar o servidor.

1. Na pasta do projeto onde está localizado o arquivo `manage.py`, execute o seguinte comando:

   ```bash
   python manage.py runserver
   ```

2. O servidor de desenvolvimento será iniciado e estará disponível em `http://127.0.0.1:8000/`.

Acesse o servidor em seu navegador e comece a explorar seu projeto.

## Desativando o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual:

```bash
deactivate
```
```