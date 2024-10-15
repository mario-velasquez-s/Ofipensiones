from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import PagosForm
from .logic import logic_pagos as lp
from django.core import serializers
from django.urls import reverse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def pagos_view(request):
    if request.method == 'GET':
        estudiante_id = request.GET.get("estudiante",None)
        if estudiante_id:
            pagos_dto = lp.get_pago_estudiante(estudiante_id)
            pago = serializers.serialize('json', [pagos_dto,])
            return HttpResponse(pago,'application/json')
        
        else:
            pagos_dto = lp.get_pagos()
            pagos = serializers.serialize('json', pagos_dto)
            return HttpResponse(pagos, 'application/json')
    
def pagos_create(request):
    if request.method == 'POST':
        form = PagosForm(request.POST)
        if form.is_valid():
            lp.create_pagos(form)
            messages.add_message(request, messages.SUCCESS, 'Pago create successful')
            return HttpResponseRedirect(reverse('pagosCreate'))
        else:
            print(form.errors)
    else:
        form = PagosForm()