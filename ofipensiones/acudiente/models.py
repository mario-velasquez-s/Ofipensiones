from django.db import models
from estudiante.models import Estudiante

class Acudiente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    relacionEstudiante = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)    


    def __str__(self):
        return '{}'.format(self.name)