from django.db import models
from django_cpf_cnpj.fields import CNPJField


# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = CNPJField(masked=True)
    #cnpj = models.CharField(max_length=30)
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=255)
    imagem = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)