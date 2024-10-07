from django.db import models

from acudiente.models import Acudiente

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    grado = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    codigo = models.IntegerField()
    estado = models.CharField(max_length=50)
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE, default=None)    


    def __str__(self):
        return '{}'.format(self.name)