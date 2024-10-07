from django.shortcuts import render
from django.http import HttpResponse
from .logic import logic_acudiente as la
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def acudiente_view(request):
    if request.method == 'GET':
        acudientes = la.get_acudientes
        acudientes_dto = serializers.serialize('json', acudientes)
        return HttpResponse(acudientes_dto, 'application/json')
    

