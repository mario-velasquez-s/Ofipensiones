from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    grado = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    codigo = models.IntegerField()
    estado = models.CharField(max_length=50)
      


    def __str__(self):
        return '{}'.format(self.codigo)