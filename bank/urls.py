from django.contrib import admin
from django.urls import path, include
from cliente import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cliente.urls'))
]
