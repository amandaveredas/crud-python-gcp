from django.db import models


# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    fabricante = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
