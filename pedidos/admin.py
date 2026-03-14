from django.contrib import admin
from .models import Cliente, Restaurante, Repartidor, Pedido


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'email', 'telefono', 'activo', 'creado_en']
    search_fields = ['nombre', 'email']
    list_filter   = ['activo']


@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'categoria', 'telefono', 'activo']
    search_fields = ['nombre', 'categoria']
    list_filter   = ['activo']


@admin.register(Repartidor)
class RepartidorAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'vehiculo', 'disponible', 'activo']
    search_fields = ['nombre']
    list_filter   = ['vehiculo', 'disponible']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display  = ['id', 'cliente', 'restaurante', 'repartidor', 'total', 'propina', 'status', 'creado_en']
    search_fields = ['cliente__nombre', 'restaurante__nombre']
    list_filter   = ['status', 'propina']
    list_editable = ['status']