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

#Instale o pacote mysqlclient:
pip install mysqlclient  

#Instale a biblioteca de cnpj:
pip install django-cpf-cnpj

#Rode o servidor:
python manage.py runserver

#Vá para o browser e digite:
http://locashost:8000
```
                                                         
# Docker:
para rodar o container:
```
docker run --name crud-empresas -d -p 8000:8000 crud-empresas:latest
```
