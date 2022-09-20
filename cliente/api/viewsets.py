from rest_framework import viewsets
from cliente.api import serializers
from cliente import models

class UsuariosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ModelSerializer
    queryset = models.Usuarios.objects.all()