from unicodedata import name
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("categorias", views.CategoriaViewSet)

urlpatterns = [
    # path('contacto/<str:nombre>', views.contacto, name='contacto'),
    # path('', views.index, name='index'),
    path('mensaje/enviar', views.enviar_mensaje),
    
    path('categorias/', views.categoria, name='categorias'),
    path('categorias/cantidad', views.categoria_contador),
    path('categorias/create_list', views.CategoriaCreateAndList.as_view(), name='categorias'),
    
    path('productos/', views.productoFormView, name='productos'),
    path('productos/reporte', views.reporte_productos),
    path('productos/tipo/unidades', views.productos_tipo_unidad),

    path('clientes/', views.clienteFormView, name= 'clientes'),
    path('clientes/cantidad', views.cliente_contador),
    path('clientes/create_list', views.ClienteCreateAndList.as_view(), name='clientes'),
    path('clientes/reporte', views.reporte_clientes),
    
    path('empresas/', views.empresaFormView, name= 'empresas'),
    path('empresas/cantidad', views.empresa_contador),
    path('empresas/create_list', views.EmpresaCreateAndList.as_view(), name='empresas'),
    path('empresas/reporte', views.reporte_empresas),
    
    path('sucursales/cantidad', views.sucursal_contador),
    path('sucursales/create_list', views.SucursalCreateAndList.as_view(), name='sucursales'),
    path('sucursales/', views.sucursalFormView, name= 'sucursales'),
    
    path('facturas/', views.facturaFormView, name= 'facturas'),
    path('facturas/cantidad', views.factura_contador),
    path('facturas/create_list', views.FacturaCreateAndList.as_view(), name='facturas'),
    
    path('detallesfacturas/cantidad', views.detallefactura_contador),
    path('detallesfacturas/create_list', views.DetalleFacturaCreateAndList.as_view(), name='detallesfacturas'),
    path('', include(router.urls))
]
