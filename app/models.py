from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=255)


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    estoque = models.IntegerField()
    preco = models.FloatField()
    status = models.CharField(max_length=255)
    empresa = models.ForeignKey("Empresa", on_delete = models.CASCADE)