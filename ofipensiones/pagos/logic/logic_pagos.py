from ..models import Pagos


def get_pagos():
    pagos = Pagos.objects.all()
    return pagos

def get_pago(pago_pk):
    pago = Pagos.objects.get(pk=pago_pk)
    return pago

def get_pago_estudiante(id_estudiante):
    pagos = Pagos.objects.filter(estudiante=id_estudiante)
    return pagos

def create_pagos(form):
    pagos = form.save()
    pagos.save()
    return()