from django.shortcuts import render
from django.http import HttpResponse
from .logic import logic_estudiante as le
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def estudiante_view(request):
    if request.method == 'GET':
        estudiantes = le.get_estudiantes
        estudiantes_dto = serializers.serialize('json', estudiantes)
        return HttpResponse(estudiantes_dto, 'application/json')
    
