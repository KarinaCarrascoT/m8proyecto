from symbol import factor
from rest_framework import serializers
from .models import Categoria
from .models import Producto
from .models import Cliente
from .models import Empresa
from .models import Sucursal
from .models import Factura
from .models import DetalleFactura
from .validators import validar_nombre_subject 
from .validators import validar_longitud_minima_texto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class ReporteProductosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    productos = ProductoSerializer(many=True)

class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100, validators=[validar_nombre_subject,])
    body = serializers.CharField(max_length=255)

class ClienteSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100, validators=[validar_nombre_subject,validar_longitud_minima_texto])
    body = serializers.CharField(max_length=255)

class ReporteClientesSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    clientes = ClienteSerializer(many=True)

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"

class ReporteEmpresasSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    empresas = EmpresaSerializer(many=True)

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"

class ReporteSucursalesSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    sucursales = SucursalSerializer(many=True)

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = "__all__"

class ReporteFacturasSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    facturas = FacturaSerializer(many=True)

class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = "__all__"

class ReporteDetallesFacturasSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    detallesfacturas = DetalleFacturaSerializer(many=True)