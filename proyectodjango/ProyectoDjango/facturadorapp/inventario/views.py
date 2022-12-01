import imp
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Categoria
from .models import Producto
from .models import Cliente
from .models import Empresa
from .models import Sucursal
from .models import Factura
from .models import DetalleFactura
from .models import Orden
from .models import OrdenProducto 
from .serializers import CategoriaSerializer
from .serializers import ProductoSerializer
from .serializers import ReporteProductosSerializer
from .serializers import ReporteClientesSerializer
from .serializers import ReporteEmpresasSerializer
from .serializers import ReporteSucursalesSerializer
from .serializers import ReporteFacturasSerializer
from .serializers import ReporteDetallesFacturasSerializer
from .serializers import ContactSerializer
from .serializers import ClienteSerializer
from .serializers import EmpresaSerializer
from .serializers import SucursalSerializer
from .serializers import FacturaSerializer
from .serializers import DetalleFacturaSerializer
from .permissions import IsUserAlmacen
from .forms import EmpresaForm, FacturaForm, ProductoForm
from .forms import ClienteForm
from .forms import SucursalForm
from .utils import permission_required
import logging

#Contacto Categoria Producto Cliente Empresa Sucursal Factura DetalleFactura
logger = logging.getLogger(__name__)
# logger = logging.getLogger("Nombre personalizado") 

def index(request):
    return HttpResponse("Hola Mundo")

def contacto(request, nombre):
    return HttpResponse(f"Bienvenido {nombre} al proyecto de Django")

def categoria(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    print(categorias.query)
    return render(request, "form_categorias.html", {"categorias": categorias})

def productoFormView(request):
    form = ProductoForm()
    producto = None
    
    id_producto = request.GET.get('id')
    if id_producto:
        # producto = Producto.objects.get(id=id_producto)
        producto = get_object_or_404(Producto, id=id_producto)
        form = ProductoForm(instance=producto)

    if request.method == 'POST':
        if producto:
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_productos.html", {"form": form})

def cliente(request):
    post_nombre = request.POST.get('razonSocial')
    if post_nombre:
        q = Cliente(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("razonSocial")
    if filtro_nombre:
        clientes = Cliente.objects.filter(nombre__contains=filtro_nombre)
    else:
        clientes = Cliente.objects.all()
    print(clientes.query)
    return render(request, "clientes.html", {"clientes": clientes})

def clienteFormView(request):
    form = ClienteForm()
    cliente = None
    
    id_cliente = request.GET.get('id')
    if id_cliente:
        # producto = Producto.objects.get(id=id_producto)
        cliente = get_object_or_404(Cliente, id=id_cliente)
        form = ClienteForm(instance=cliente)

    if request.method == 'POST':
        if cliente:
            form = ClienteForm(request.POST, instance=cliente)
        else:
            form = ClienteForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_clientes.html", {"form": form})


def empresa(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Empresa(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        empresas = Empresa.objects.filter(nombre__contains=filtro_nombre)
    else:
        empresas = Empresa.objects.all()
    print(empresas.query)
    return render(request, "empresas.html", {"empresas": empresas})

def empresaFormView(request):
    form = EmpresaForm()
    empresa = None
    
    id_empresa = request.GET.get('id')
    if id_empresa:
        # producto = Producto.objects.get(id=id_producto)
        empresa = get_object_or_404(Cliente, id=id_empresa)
        form = EmpresaForm(instance=empresa)

    if request.method == 'POST':
        if empresa:
            form = EmpresaForm(request.POST, instance=empresa)
        else:
            form = EmpresaForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_empresas.html", {"form": form})

def sucursal(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Sucursal(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        sucursales = Sucursal.objects.filter(nombre__contains=filtro_nombre)
    else:
        sucursales = Sucursal.objects.all()
    print(sucursales.query)
    return render(request, "sucursales.html", {"sucursales": sucursales})

def sucursalFormView(request):
    form = SucursalForm()
    sucursal = None
    
    id_sucursal = request.GET.get('id')
    if id_sucursal:
        # producto = Producto.objects.get(id=id_producto)
        sucursal = get_object_or_404(Sucursal, id=id_sucursal)
        form = SucursalForm(instance=sucursal)

    if request.method == 'POST':
        if sucursal:
            form = SucursalForm(request.POST, instance=sucursal)
        else:
            form = SucursalForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_sucursales.html", {"form": form})

def factura(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Factura(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        facturas = Factura.objects.filter(nombre__contains=filtro_nombre)
    else:
        facturas = Factura.objects.all()
    print(facturas.query)
    return render(request, "facturas.html", {"facturas": facturas})

def facturaFormView(request):
    form = FacturaForm()
    factura = None
    
    id_factura = request.GET.get('id')
    if id_factura:
        # producto = Producto.objects.get(id=id_producto)
        factura = get_object_or_404(Factura, id=id_factura)
        form = FacturaForm(instance=factura)

    if request.method == 'POST':
        if factura:
            form = FacturaForm(request.POST, instance=factura)
        else:
            form = FacturaForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_facturas.html", {"form": form})

def detallefactura(request):
    post_nombre = request.POST.get('nomb    re')
    if post_nombre:
        q = detallefactura(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        detallefacturas = DetalleFactura.objects.filter(nombre__contains=filtro_nombre)
    else:
        detallefacturas = DetalleFactura.objects.all()
    print(detallefacturas.query)
    return render(request, "detallefacturas.html", {"facturas": detallefacturas})

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #permission_classes = [IsUserAlmacen]

#@permission_classes([IsAuthenticated])
class CategoriaCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(["GET"])
## @permission_classes([IsAuthenticated])
#@permission_required(["inventario.reporte_cantidad"])
def categoria_contador(request):
    """
    Cantidad de items en el modelo categoria
    """
    logger.info("Cantidad categoria mostada correctamente")
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

@api_view(["GET"])
def cliente_contador(request):
    """
    Cantidad de items en el modelo clientes
    """
    logger.info("Cantidad cliente mostrada correctamente")
    try:
        cantidad = Cliente.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def factura_contador(request):
    """
    Cantidad de items en el modelo facturas
    """
    logger.info("Cantidad facturas mostrada correctamente")
    try:
        cantidad = Factura.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

class FacturaCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

@api_view(["GET"])
def detallefactura_contador(request):
    """
    Cantidad de items en el modelo detallefactura
    """
    logger.info("Cantidad detales facturas mostrada correctamente")
    try:
        cantidad = DetalleFactura.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

class DetalleFacturaCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

@api_view(["GET"])
def empresa_contador(request):
    """
    Cantidad de items en el modelo empresa
    """
    logger.info("Cantidad empresas mostrada correctamente")
    try:
        cantidad = Empresa.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class SucursalCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

@api_view(["GET"])
def sucursal_contador(request):
    """
    Cantidad de items en el modelo sucursal
    """
    logger.info("Cantidad sucursales mostrada correctamente")
    try:
        cantidad = Sucursal.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)


@api_view(["GET"])
def productos_tipo_unidad(request):
    """
    Productos filtrados por tipo de unidad
    """
    try:
        productos = Producto.objects.filter(unidades='u')
        return JsonResponse(
            ProductoSerializer(productos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_productos(request):
    """
    Reporte de productos
    """
    try:
        productos = Producto.objects.filter(unidades='u')
        cantidad = productos.count()

        return JsonResponse(
            ReporteProductosSerializer({
                "cantidad": cantidad,
                "productos": productos
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_clientes(request):
    """
    Reporte de clientes
    """
    try:
        clientes = Empresa.objects.all()
        cantidad = clientes.count()

        return JsonResponse(
            ReporteClientesSerializer({
                "cantidad": cantidad,
                "clientes": clientes
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_empresas(request):
    """
    Reporte de empresas
    """
    try:
        empresas = Empresa.objects.all()
        cantidad = empresas.count()

        return JsonResponse(
            ReporteEmpresaSerializer({
                "cantidad": cantidad,
                "empresas": empresas
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_sucursales(request):
    """
    Reporte de sucursales
    """
    try:
        sucursales = Sucursal.objects
        cantidad = sucursales.count()

        return JsonResponse(
            ReporteSucursalesSerializer({
                "cantidad": cantidad,
                "sucursales": sucursales
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)


@api_view(["GET"])
def reporte_facturas(request):
    """
    Reporte de facturas
    """
    try:
        facturas = Factura.objects
        cantidad = facturas.count()

        return JsonResponse(
            ReporteSucursalesSerializer({
                "cantidad": cantidad,
                "facturas": facturas
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_detallesfacturas(request):
    """
    Reporte de detallesfacturas
    """
    try:
        detallesfacturas = DetalleFactura.objects.filter();
        cantidad = detallesfacturas.count()

        return JsonResponse(
            ReporteDetallesFacturasSerializer({
                "cantidad": cantidad,
                "detallesfacturas": detallesfacturas
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["POST"])
def enviar_mensaje(request):
    """
    Enviar mensajes via email
    """
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({"mensaje": "Mensaje enviado satisfactoriamente"}, status=200)
    else:
        return JsonResponse({"mensaje": cs.errors}, status=200)


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = DetalleFacturaSerializer
