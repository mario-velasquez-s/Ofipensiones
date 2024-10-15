from django import forms 
from .models import Pagos

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = [
            'codigoPago',
            'monto',
            'fechaPago',
            'estudiante',
            'acudiente'
        ]

        labels = {
            'codigoPago' : 'Codigo Pago',
            'monto' : 'Monto',
            'fechaPago' : 'Fecha Pago',
            'estudiante' : 'Estudiante',
            'acudiente' : 'Acudiente',
        }