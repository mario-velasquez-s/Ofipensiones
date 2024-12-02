from django.db import models

from django.db import models
from estudiante.models import Estudiante
from acudiente.models import Acudiente

class IntegracionContable(models.Model):
    codigoIntegracion = models.BigIntegerField()
    fechaGeneracion = models.DateField(auto_now_add=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    paz_y_salvo = models.BooleanField(default=False)

    def __str__(self):
        return f'Integración {self.codigoIntegracion}'

