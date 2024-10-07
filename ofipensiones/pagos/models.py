from django.db import models

class Pagos(models.Model):
    codigoPago = models.BigIntegerField()
    monto = models.BigIntegerField()
    fechaPago = models.DateField()
    estudiante = models.BigIntegerField()
    padre = models.BigIntegerField()
    


    def __str__(self):
        return '{}'.format(self.name)