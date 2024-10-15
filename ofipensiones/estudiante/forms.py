from django import forms 
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre',
            'grado',
            'fechaNacimiento',
            'codigo',
            'estado',
        ]
        labels = {
            'nombre' : 'Nombre',
            'grado' : 'Grado',
            'fechaNacimiento': 'Fecha Nacimiento',
            'codigo' : 'Codigo',
            'estado' : 'Estado',
        }