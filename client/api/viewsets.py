from rest_framework import viewsets
from client.api import serializers
from client import models

class ClienteViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()