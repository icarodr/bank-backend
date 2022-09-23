from django.db import models


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
    
    id_cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name='usuarios', 
        blank=False, null=False
        )

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
    
    id_cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name='enderecos', 
        blank=False, null=False
        )
    LOG_CHOICES = (
        ("C","Casa"),
        ("A","Apartamento")
    )
    #RELACIONA COM CLIENTE

class Contatos(models.Model):
    telefone = models.CharField(max_length=12)
    email = models.EmailField(null=False, blank=False)
    
    id_cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name='contatos', 
        blank=False, null=False
        )
    #RELACIONAMENTO COM CLIENTE

class Favoritos(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    
    id_cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name='favoritos', 
        blank=False, null=False
        )
    #RELACIONAR COM CLIENTE

class Transacoes(models.Model):
    valor = models.FloatField()
    data = models.DateField()
    
    id_cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name='transacoes', 
        blank=False, null=False
        )
    #RELACIONAR COM CLIENTE


class Conta(models.Model):
    saldo = models.FloatField(null=False, blank=False)
    salario = models.FloatField(null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    
    id_cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name='conta', 
        blank=False, null=False)

    TIPO_CHOICES = (
        ("C","Corrente"),
        ("P","Poupança"),
        ("S","Salário")
    )

    def __str__(self):
        return self.saldo
    #RELACIONAR COM CLIENTE

class Emprestimo(models.Model):
    valor = models.FloatField(null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    juros = models.FloatField(null=False, blank=False)
    validade = models.DateField(null=False, blank=False)
    condicao = models.BooleanField(null=False, blank=False)
    
    id_conta = models.ForeignKey(
        Conta, 
        on_delete=models.PROTECT, 
        related_name='emprestimo', 
        blank=False, null=False
        )


class Cartoes(models.Model):
    numero = models.CharField(max_length=16, null=False, blank=False)
    cvv = models.CharField(max_length=3, null=False, blank=False)
    data_validade = models.DateField(null=False, blank=False)
    estado = models.BooleanField(null=False, blank=False)
    TIPO_CARTAO_CHOICES = (
        ("C","Credito"),
        ("D","Debito")
    )
    
    id_conta = models.ForeignKey(
        Conta, 
        on_delete=models.PROTECT, 
        related_name='cartoes', 
        blank=False, null=False
        )


class Fatura(models.Model):
    valor = models.CharField(max_length=100)
    data_pagamento = models.DateField()
    data_pago = models.DateField()
    
    id_cartoes = models.ForeignKey(
        Cartoes, 
        on_delete=models.PROTECT, 
        related_name='fatura', 
        blank=False, null=False
        )