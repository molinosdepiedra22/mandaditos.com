from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cliente, Restaurante, Repartidor, Pedido
from .forms import ClienteForm, RestauranteForm, RepartidorForm, PedidoForm


# REGISTRAR
def registrar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente registrado correctamente.')
        return redirect('registrar_cliente')
    return render(request, 'pedidos/registrar.html', {'form': form, 'titulo': 'Registrar Cliente'})

def registrar_restaurante(request):
    form = RestauranteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Restaurante registrado correctamente.')
        return redirect('registrar_restaurante')
    return render(request, 'pedidos/registrar.html', {'form': form, 'titulo': 'Registrar Restaurante'})

def registrar_repartidor(request):
    form = RepartidorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Repartidor registrado correctamente.')
        return redirect('registrar_repartidor')
    return render(request, 'pedidos/registrar.html', {'form': form, 'titulo': 'Registrar Repartidor'})

def registrar_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pedido registrado correctamente.')
        return redirect('registrar_pedido')
    return render(request, 'pedidos/registrar.html', {'form': form, 'titulo': 'Registrar Pedido'})


# EDITAR
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente actualizado correctamente.')
        return redirect('editar_cliente', pk=pk)
    return render(request, 'pedidos/editar.html', {'form': form, 'titulo': 'Editar Cliente', 'objeto': cliente})

def editar_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    form = RestauranteForm(request.POST or None, instance=restaurante)
    if form.is_valid():
        form.save()
        messages.success(request, 'Restaurante actualizado correctamente.')
        return redirect('editar_restaurante', pk=pk)
    return render(request, 'pedidos/editar.html', {'form': form, 'titulo': 'Editar Restaurante', 'objeto': restaurante})

def editar_repartidor(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    form = RepartidorForm(request.POST or None, instance=repartidor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Repartidor actualizado correctamente.')
        return redirect('editar_repartidor', pk=pk)
    return render(request, 'pedidos/editar.html', {'form': form, 'titulo': 'Editar Repartidor', 'objeto': repartidor})

def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pedido actualizado correctamente.')
        return redirect('editar_pedido', pk=pk)
    return render(request, 'pedidos/editar.html', {'form': form, 'titulo': 'Editar Pedido', 'objeto': pedido})


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