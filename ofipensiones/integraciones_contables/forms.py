from django import forms
from .models import IntegracionContable

class IntegracionContableForm(forms.ModelForm):
    class Meta:
        model = IntegracionContable
        fields = [
            'codigoIntegracion',
            'estudiante',
            'acudiente',
            'paz_y_salvo',
        ]
        labels = {
            'codigoIntegracion': 'Código de Integración',
            'estudiante': 'Estudiante',
            'acudiente': 'Acudiente',
            'paz_y_salvo': 'Paz y Salvo',
        }
