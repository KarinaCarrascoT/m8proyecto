from django import forms
from .models import Producto
from .models import Cliente
from .models import Empresa
from .models import Sucursal
from .models import Factura
from .models import DetalleFactura

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = "__all__"

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = "__all__"

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = "__all__"

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = "__all__"
