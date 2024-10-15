from ..models import Acudiente

def get_acudientes():
    acudientes = Acudiente.objects.all()
    return acudientes


def create_estudiante(form):
    acudiente = form.save()
    acudiente.save()
    return ()