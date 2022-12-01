from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from .validators import validar_par 
from .validators import validar_nombre_categoria 
from .validators import validar_cantidad_minima_items_factura
from .validators import validar_longitud_minima_texto
from django.core.validators import EmailValidator 


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre_categoria,]) 
    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("reporte_cantidad", "Visualizar el reporte de cantidad"),
            ("reporte_detalle", "Reporte detallado de cantidades"),
        ]

class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    description = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_par,])
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Producto - %s" % self.nombre

class EstadoOrden(models.TextChoices):
    NOPAGADO = 'nopagado', 'No Pagado'
    PAGADO = 'pagado', 'Pagado'

class Orden(models.Model):
    total = models.IntegerField(default=0)
    fecha = models.DateField()
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventario_orden_vendedor"
    )
    estado = models.CharField(
        max_length=10,
        choices=EstadoOrden.choices,
        default=EstadoOrden.NOPAGADO
    )

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(decimal_places=2, max_digits=10)


class Cliente(models.Model):
    razonSocial =  models.CharField(max_length=50, unique=True, validators=[validar_longitud_minima_texto,])
    primerApellido =  models.CharField(max_length=30)
    segundoApellido =  models.CharField(max_length=30)
    primerNombre =  models.CharField(max_length=30)
    otrosNombre =  models.CharField(max_length=30)
    email =  models.EmailField(max_length=30)
    documento =  models.CharField(max_length=20, unique=True)
    estado = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cliente - %s" % self.razonSocial

class Empresa(models.Model):
    razonSocial = models.CharField(max_length=20, unique=True),
    nitEmisor = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Empresa - %s" % self.razonSocial

class Sucursal(models.Model):
    numero = models.IntegerField(unique = True)
    municipio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    esCasaMatriz = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Sucursal - %s" % self.direccion

class EstadoFactura(models.TextChoices):
    VALIDA = 'valida', 'Válida'
    ANULADA = 'anulada', 'Anulada'

class MetodoPago(models.TextChoices):
    CONTADO = 'contado', 'Contado'
    CREDITO = 'credito', 'Crédito'

class Factura(models.Model):
    numeroFactura = models.IntegerField(default=1)
    cuf = models.CharField(
        max_length = 52
    )
    fecha = models.DateField()
    nombreRazonSocial = models.CharField,
    codigoTipoDocumentoIdentidad = models.CharField,
    numeroDocumento = models.CharField,
    complemento = models.CharField,
    metodoPago = models.CharField(
        max_length=10,
        choices=MetodoPago.choices,
        default=MetodoPago.CONTADO
    )
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE) 
    
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventario_factura_cliente"
    )
    montoTotal = models.IntegerField(default=0)
    montoTotalSujetoIva = models.IntegerField(default=0)
    estado = models.CharField(
        max_length=10,
        choices=EstadoFactura.choices,
        default=EstadoFactura.VALIDA
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Factura - %s" % self.cuf

class DetalleFactura(models.Model):
    Factura = models.ForeignKey(Factura, on_delete=models.CASCADE) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    cantidad = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_cantidad_minima_items_factura,])
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        permissions = [
            ("reporte_cantidad_items_factura", "Visualizar el reporte de cantidad items factura"),
            ("reporte_detalle_items_factura", "Reporte detalle items factura"),
        ]
