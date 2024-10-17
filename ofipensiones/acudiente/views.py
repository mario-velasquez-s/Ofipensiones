from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .logic import logic_acudiente as la
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import AcudienteForm
from django.contrib import messages
from django.urls import reverse

@csrf_exempt
def acudiente_view(request):
    if request.method == 'GET':
        acudientes = la.get_acudientes()
        acudientes_dto = serializers.serialize('json', acudientes)
        return HttpResponse(acudientes_dto, 'application/json')
    

def acudiante_create(request):
    if request.method == 'POST':
        form = AcudienteForm(request.POST)
        if form.is_valid():
            la.create_estudiante(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created estudiante')
            return HttpResponseRedirect(reverse('estudianteCreate'))
        else:
            print(form.errors)
    
    
