from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cliente, Restaurante, Repartidor, Pedido
from .forms import ClienteForm, RestauranteForm, RepartidorForm, PedidoForm


# REGISTRAR 
def registrar_cliente(request):
    return render(request, 'pedidos/registrar.html')

def registrar_restaurante(request):
    pass

def registrar_repartidor(request):
    pass

def registrar_pedido(request):
    pass


# EDITAR
def editar_cliente(request, pk):
    pass

def editar_restaurante(request, pk):
    pass

def editar_repartidor(request, pk):
    pass

def editar_pedido(request, pk):
    pass


# STATUS 

def cambiar_status(request, pk):
    pass


# PROPINAS
def gestionar_propina(request, pk):
    pass


# ELIMINAR 
def eliminar_cliente(request, pk):
    pass

def eliminar_restaurante(request, pk):
    pass

def eliminar_repartidor(request, pk):
    pass

def eliminar_pedido(request, pk):
    pass


# RATING
def rating_cliente(request, pk):
    pass

def rating_restaurante(request, pk):
    pass

def rating_repartidor(request, pk):
    pass