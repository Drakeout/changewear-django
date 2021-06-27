from core.models import Cliente
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(ProductoCompra)
admin.site.register(DireccionEnvio)

