from django.contrib import admin
from django.urls import path, include
from client.api import viewsets as clientviewsets
from rest_framework import routers


route = routers.DefaultRouter()
route.register(r'client', clientviewsets.ClienteViewset, basename='Client')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
