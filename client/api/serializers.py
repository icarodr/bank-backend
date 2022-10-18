from dataclasses import fields
from rest_framework import serializers
from client import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = '__all__'

class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contatos
        fields = '__all__'

class FavoritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Favoritos
        fields = '__all__'

class TransacoesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Transacoes
        fields = '__all__'

class ContaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Conta
        fields = '__all__'

class EmprestimoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Emprestimo
        fields = '__all__'

class CartoesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cartoes
        fields = '__all__'

class FaturaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Fatura
        fields = '__all__'

        