from rest_framework import viewsets
from .serializers import serializers
from cliente import models

class UsuariosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ModelSerializer
    queryset = models.Cliente.objects.all()