from django.urls import path
from web_1.views import *


urlpatterns = [
    path('', inicio, name = "web-1-inicio"),
    path('ingresar_producto/', carga_productos, name = "web-1-carga-productos"),
    path('ingresar_usuario/', carga_usuarios, name = "web-1-carga-usuarios"),
    path('ingresar_vendedor/', carga_empresas, name = "web-1-carga-empresas")
]