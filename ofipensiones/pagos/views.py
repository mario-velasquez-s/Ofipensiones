from django.shortcuts import render
from django.http import HttpResponse
from .logic import logic_pagos as lp
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def pagos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id",None)
        if id:
            pagos_dto = lp.get_pago(id)
            pago = serializers.serialize('json', [pagos_dto,])
            return HttpResponse(pago,'application/json')
        
        else:
            pagos_dto = lp.get_pagos()
            pagos = serializers.serialize('json', pagos_dto)
            return HttpResponse(pagos, 'application/json')
    
