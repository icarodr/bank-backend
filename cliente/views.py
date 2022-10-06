from django.shortcuts import render
from django import views
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets
from rest_framework import status
from cliente.models import Cliente, Usuario, Endereco, Conta, Contatos, Cartoes, Fatura, Favoritos
from rest_framework.response import Response

# Create your views here.

