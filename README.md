# SISTEMA DE CADASTRO HOP[P]ERS
<div align="center">
<img src = "https://i.imgur.com/OuuUJnl.jpg" width=500px'>
</div>


O Sistema de cadastro Hop[p]ers é uma aplicação web construída com o objetivo de facilitar o gerenciamento de estoque de empresas do varejo através dos serviços de:

- Cadastrar Empresas e Produtos;
- Listar Empresas e Produtos;
- Adicionar um novo produto na lista da Empresa;
- Atualizar informações do produto;
- Remover produtos da lista da Empresa;
- Consultar todos os produtos e empresas cadastradas.

# Modelo lógico:

<div align="start">
<img src = "https://i.imgur.com/3k2nPCt.png" width=550px'>
</div>

# Tecnologias utilizadas:
Back-end:
- Python
- Django
- MySQL

Front-end:
- HTML
- CSS
- Bootstrap
- Javascript

Deploy
- Jenkins
- Docker
- Kubernetes

# Como executar o projeto localmente:

```text
#Execute o seguinte comando no terminal para clonar o repositório:
git clone https://github.com/amandaveredas/crud-python-gcp.git


#Na pasta do projeto, ative a máquina virtual:
venv\Scripts\activate

#Instale a biblioteca de cnpj:
pip install django-cpf-cnpj

#Rode o servidor:
python manage.py runserver

#Vá para o browser e digite:
http://locashost:8000
```
# Rodando o banco de dados:

Utilização do WampServer como servidor do MySQL (Windows):
WampServer

Para sistemas Linux, usar o LAMP

Baixar a versão correspondendo a versão do sistema operacional (32bit ou 64bit);
Acessar localhost/phpmyadmin para ver a interface do banco MySQL

User: root

Password: apenas pressionar enter

obs: nome da tabela: sistemahp

Se necessário atualizar a versão do MySQL:
Python Extension Packages for Windows - Christoph Gohlke

Buscar a versão do Python (cp37 para python 3.7, cp38 para 3.8, cp39 para 3.9) compatível com a versão do Windows;

Baixar e colocar na pasta do aplicativo;

No prompt, iniciar o python e usar o comando:

pip install "nome da versão"

ex:

pip install mysqlclient-1.4.6-cp39-cp39-win_amd64.whl

finalizar com:

python manage.py migrate

                                                         
# Docker:
para rodar o container:
```
docker pull amandaveredas/crud-empresas:latest
docker run --name crud-empresas -d -p 8000:8000 crud-empresas:latest
```
