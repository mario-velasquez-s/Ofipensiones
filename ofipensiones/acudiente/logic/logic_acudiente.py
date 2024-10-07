from ..models import Acudiente

def get_acudientes():
    acudientes = Acudiente.objects.all()
    return acudientes