from django import forms 
from .models import Acudiente

class AcudienteForm(forms.ModelForm):
    class Meta:
        model = Acudiente
        fields = [
            'nombre',
            'telefono',
            'email',
            'direccion',
            'relacionEstudiante',
            'estudiante',
        ]
        labels = {
            'nombre' : 'Nombre',
            'telefono' : 'Telefono',
            'email' : 'Email',
            'direccion' : 'Direccion',
            'relacionEstudiante' : 'Relacion Estudiante',
            'estudiante' : 'Estudiante',
        }