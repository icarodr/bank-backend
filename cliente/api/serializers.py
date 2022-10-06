from rest_framework import serializers
from cliente import models

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class EnderecoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = '__all__'

class ContatoSerializers(serializers.ModelSerializer):
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

class CartoeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cartoes
        fields = '__all__'

class FaturaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Fatura
        fields = '__all__'