from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=255, null=False, blank=False)
    data_nasc = models.DateField()
    trabalhando = models.BooleanField()
    GENERO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    
    def __str__(self):
        return self.nome_completo

class Usuario(models.Model):
    senha = models.CharField(max_length=10, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)

    def __str__(self):
        return self.senha
    #RELACIONA COM CLIENTE

class Endereco(models.Model):
    pais = models.CharField(max_length=255, null=False, blank=False)
    uf = models.CharField(max_length=2, null=False, blank=False)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    bairro = models.CharField(max_length=255, null=False, blank=False)
    rua = models.CharField(max_length=255, null=False, blank=False)
    numero = models
    cep = models.CharField(max_length=8)
    LOG_CHOICES = (
        ("C","Casa"),
        ("A","Apartamento")
    )
    #RELACIONA COM CLIENTE

class Contatos(models.Model):
    telefone = models.CharField(max_length=12)
    email = models.EmailField(null=False, blank=False)
    #RELACIONAMENTO COM CLIENTE

class Conta(models.Model):
    saldo = models.FloatField(null=False, blank=False)
    salario = models.FloatField(null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    TIPO_CHOICES = (
        ("C","Corrente"),
        ("P","Poupança"),
        ("S","Salário")
    )

    def __str__(self):
        return self.saldo

class Cartoes(models.Model):
    numero = models.CharField(max_length=16, null=False, blank=False)
    cvv = models.CharField(max_length=3, null=False, blank=False)
    data_validade = models.DateField(null=False, blank=False)
    estado = models.BooleanField(null=False, blank=False)
    TIPO_CARTAO_CHOICES = (
        ("C","Credito"),
        ("D","Debito")
    )

class Fatura(models.Model):
    valor = models.CharField(max_length=100)
    data_pagamento = models.DateField()
    data_pago = models.DateField()
