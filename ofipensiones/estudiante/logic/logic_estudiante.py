from ..models import Estudiante

def get_estudiantes():
    estudiantes = Estudiante.objects.all()
    return estudiantes

def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()