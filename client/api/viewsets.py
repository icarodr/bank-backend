from rest_framework import viewsets
from client.api import serializers
from client import models

class ClienteViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()

class UsuariosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.UsuariosSerializer
    queryset = models.Usuario.objects.all()

class EnderecoViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.EnderecoSerializer
    queryset = models.Endereco.objects.all()

class ContatosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ContatosSerializer
    queryset = models.Contatos.objects.all()

class FavoritosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.FavoritosSerializers
    queryset = models.Favoritos.objects.all()

class TransacoesViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.TransacoesSerializers
    queryset = models.Transacoes.objects.all()

class ContaViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ContaSerializers
    queryset = models.Conta.objects.all()

class EmprestimoViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.EmprestimoSerializers
    queryset = models.Emprestimo.objects.all()

class CartoesViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.CartoesSerializers
    queryset = models.Cartoes.objects.all()

class FaturaViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.FaturaSerializers
    queryset = models.Fatura.objects.all()