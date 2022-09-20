from django.db import models

# Create your models here.
class Usuarios(models.Model):
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=255)
    block = models.BooleanField()

class Cadastro(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dataNascimento = models.DateField()
    genero = models.CharField(max_length=255)

class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    