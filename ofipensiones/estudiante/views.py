from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .logic import logic_estudiante as le
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import EstudianteForm
from django.contrib import messages
from django.urls import reverse
from .forms import EstudianteForm

@csrf_exempt
def estudiante_view(request):
    if request.method == 'GET':
        estudiantes = le.get_estudiantes
        estudiantes_dto = serializers.serialize('json', estudiantes)
        return HttpResponse(estudiantes_dto, 'application/json')
    

def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            le.create_estudiante(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created estudiante')
            return HttpResponseRedirect(reverse('estudianteCreate'))
        else:
            print(form.errors)
    else:
        form = EstudianteForm()

    
