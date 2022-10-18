from django.contrib import admin
from django.urls import path, include
from client.api import viewsets as clientviewsets
from rest_framework import routers


route = routers.DefaultRouter()
route.register(r'cliente', clientviewsets.ClienteViewSets, basename='Client')
route.register(r'usuarios', clientviewsets.UsuariosViewSets, basename='Usuarios')
route.register(r'endereco', clientviewsets.EnderecoViewSets, basename='Endereco')
route.register(r'contatos', clientviewsets.ContatosViewSets, basename='Contatos')
route.register(r'favoritos', clientviewsets.FavoritosViewSets, basename='Favoritos')
route.register(r'transacoes', clientviewsets.TransacoesViewSets, basename='Transacoes')
route.register(r'conta', clientviewsets.ContaViewSets, basename='Conta')
route.register(r'emprestimo', clientviewsets.EmprestimoViewSets, basename='Emprestimo')
route.register(r'cartoes', clientviewsets.CartoesViewSets, basename='Cartoes')
route.register(r'fatura', clientviewsets.FaturaViewSets, basename='Fatura')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
