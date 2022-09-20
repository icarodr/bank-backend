from rest_framework import serializers
from cliente import models

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usuarios
        fields = '__all__'