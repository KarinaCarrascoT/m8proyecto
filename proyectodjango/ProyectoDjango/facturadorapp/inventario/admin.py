from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Orden
from .models import OrdenProducto
from .models import Cliente
from .models import Empresa
from .models import Sucursal
from .models import Factura
from .models import DetalleFactura


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades")
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible","precio")

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("razonSocial","primerApellido", "segundoApellido", "primerNombre", "otrosNombre", "email", "documento", "estado")
    ordering = ["primerNombre"]
    search_fields = ["razonSocial","primerApellido", "segundoApellido", "primerNombre", "otrosNombre"]
    list_filter = ("razonSocial","documento","primerApellido", "segundoApellido", "primerNombre", "otrosNombre")

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden)
admin.site.register(OrdenProducto)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
