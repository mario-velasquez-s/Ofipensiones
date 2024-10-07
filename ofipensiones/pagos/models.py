from django.db import models
from estudiante.models import Estudiante
from acudiente.models import Acudiente

class Pagos(models.Model):
    codigoPago = models.BigIntegerField()
    monto = models.BigIntegerField()
    fechaPago = models.DateField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.DO_NOTHING)
    acudiente = models.ForeignKey(Acudiente, on_delete=models.DO_NOTHING)


    def __str__(self):
        return '{}'.format(self.name)