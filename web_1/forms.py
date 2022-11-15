from django import forms


class Usuario_formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()
    contraseña = forms.CharField()


class Productos_formulario(forms.Form):
    sku = forms.IntegerField()
    nombre = forms.CharField()
    precio = forms.DecimalField()
    stock = forms.IntegerField()


class Vendedores_formulario(forms.Form):
    nombre_empresa = forms.CharField()
    marca = forms.CharField()
    rubro = forms.CharField()