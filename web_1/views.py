from django.shortcuts import render
from web_1.models import *
from web_1.forms import *

# Create your views here.

def inicio(request):
    return render(request, r"web_1\index.html")

#Formularios de carga

def carga_productos(request):
    
    if request.method == "POST":
        
        formulario  = Productos_formulario(request.POST)

        if formulario.is_valid():
            
            info_producto=formulario.cleaned_data

            producto = Productos(sku=info_producto["sku"], nombre=info_producto["sku"], precio=info_producto["precio"], stock=info_producto["stock"])

            producto.save()

        return render(request, r"web_1\index.html")
    else:
        formulario = Productos_formulario()
    
    contexto = {"formulario":formulario}
    
    return render(request, r"web_1\producto_formulario.html", contexto)


def carga_usuarios(request):
    if request.method == "POST":
        
        formulario  = Usuario_formulario(request.POST)

        if formulario.is_valid():
            
            info_usuario=formulario.cleaned_data

            producto = Usuario(nombre=info_usuario["nombre"], apellido=info_usuario["apellido"], mail=info_usuario["mail"], contraseña=info_usuario["contraseña"])

            producto.save()

        return render(request, r"web_1\index.html")
    else:
        formulario = Usuario_formulario()
    
    contexto = {"formulario":formulario}
    
    return render(request, r"web_1\usuario_formulario.html", contexto)

def carga_empresas(request):
    if request.method == "POST":
        
        formulario  = Vendedores_formulario(request.POST)

        if formulario.is_valid():
            
            info_vendedor=formulario.cleaned_data

            producto = Vendedores(nombre_empresa=info_vendedor["nombre_empresa"], marca=info_vendedor["marca"], rubro=info_vendedor["rubro"])

            producto.save()

        return render(request, r"web_1\index.html")
    else:
        formulario = Vendedores_formulario()
    
    contexto = {"formulario":formulario}
    
    return render(request, r"web_1\vendedores_formularios.html", contexto)
