from ..models import IntegracionContable

def get_integraciones():
    return IntegracionContable.objects.all()

def get_integracion(integracion_pk):
    return IntegracionContable.objects.get(pk=integracion_pk)

def get_integraciones_estudiante(id_estudiante):
    return IntegracionContable.objects.filter(estudiante=id_estudiante)

def create_integracion(form):
    integracion = form.save()
    integracion.save()
