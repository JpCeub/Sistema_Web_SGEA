SGEA - Projeto Django (protótipo)
Sistema de Gestão de Eventos Acadêmicos desenvolvido em Django, permitindo gerenciar eventos, inscrições, emissão de certificados e controle de usuários.

Funcionalidades Principais:
-Cadastro e gerenciamento de eventos
-Controle de inscrições de participantes
-Emissão e validação de certificados
-Autenticação e gerenciamento de usuários

Tecnologias Utilizadas:
-Python 3.x
-Django 4.x
-SQLite3 (banco de dados padrão)
-HTML, CSS, JavaScript (templates e front-end)
-Interface web simples e responsiva

Estrutura criada:
- apps: usuarios, eventos, inscricoes, certificados
- banco: SQLite (preparado em settings.py)
- templates simples em templates/

Como rodar (no Windows, no VS Code ou terminal):

Baixe a pasta do projeto pelo link do repositório no GitHub

Entre na pasta do projeto:
cd Sistema_Web_SGEA/Sistema_Web_SGEA


Crie o ambiente virtual:
python -m venv venv


Ative o ambiente:
.\venv\Scripts\activate


Instale as dependências:
pip install -r requirements.txt


Execute as migrações:
python manage.py makemigrations

python manage.py migrate


Rode o servidor:
python manage.py runserver

Popular o bando de dados:
python populate.py

Apos a execução do comando:
- Cria um usuário organizador (organizador@sgea.com, senha 123456)
- Apaga eventos antigos
- insere 4 eventos novos (um de cada tipo)

Acesse no navegador:
http://127.0.0.1:8000/

Observações:
- Este projeto é um protótipo com formulários e templates mínimos.

- O banco de dados e o diagrama possuem algumas tabelas e atributos diferentes. Isso se deve a algumas funções nativas do Django que utilizamos no código, como o AbstractUser para criar os campos de nome, senha e e-mail do usuário, o que acabou adicionando algumas tabelas e atributos que não foram utilizados, mas que, caso sejam removidos, deixam o código comprometido.


Autores:

João Pedro Roriz Costa
RA: 22404348

Arthur de Jesus Lira Rojas
RA: 22404292

Arthur Dantas de Araújo Pessoa
RA: 22402868