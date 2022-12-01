from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s no es un numero par',
            params={'value': value}
        )

def validar_nombre_categoria(value):
    if value == 'No permitido':
        raise ValidationError("No es una opcion permitida")

def validar_nombre_subject(value):
    if value == 'Comida':
        raise ValidationError("No es una opcion permitida")

def validar_longitud_minima_texto(value):
    if len(value) < 3:
        raise ValidationError("El texto debe tener más de 3 letras")

def validar_cantidad_minima_items_factura(value):
    if value < 1:
        raise ValidationError("La cantidad de items debe ser mayor a 1")