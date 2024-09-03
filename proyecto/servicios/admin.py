from django.contrib import admin
from .models import Cliente, Servicio, Pedido

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Pedido)