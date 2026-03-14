from django import forms
from .models import Cliente, Restaurante, Repartidor, Pedido


class ClienteForm(forms.ModelForm):
    class Meta:
        model  = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion', 'activo']


class RestauranteForm(forms.ModelForm):
    class Meta:
        model  = Restaurante
        fields = ['nombre', 'direccion', 'telefono', 'categoria', 'activo']


class RepartidorForm(forms.ModelForm):
    class Meta:
        model  = Repartidor
        fields = ['nombre', 'telefono', 'vehiculo', 'disponible', 'activo']


class PedidoForm(forms.ModelForm):
    class Meta:
        model  = Pedido
        fields = ['cliente', 'restaurante', 'repartidor', 'descripcion', 'total', 'propina', 'status']