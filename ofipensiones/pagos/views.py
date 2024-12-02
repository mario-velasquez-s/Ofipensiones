from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from ofipensiones.auth0backend import getRole, get_email
from .forms import PagosForm
from .logic import logic_pagos as lp
from django.core import serializers
import json
<<<<<<< HEAD
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

=======
>>>>>>> 1875596cd70af87c17b27b60893856cce4c85f6d

@login_required
@csrf_exempt
def pagos_view(request):
    role = getRole(request)
    email = get_email(request)
    
    # Verificar si el usuario es administrador o tiene el correo permitido
    if role == "Administrador de Pagos" or email == "rector@colegio.com":
        if request.method == 'GET':
            pagos_dto = lp.get_pagos()
            pagos = serializers.serialize('json', pagos_dto)
            return HttpResponse(pagos, 'application/json')
<<<<<<< HEAD
    
@login_required
@csrf_exempt
def pagos_create(request):
    if request.method == 'POST':
        form = PagosForm(request.POST)
        if form.is_valid():
            lp.create_pagos(form)
            messages.add_message(request, messages.SUCCESS, 'Pago create successful')
            return HttpResponseRedirect(reverse('pagos_view'))
=======
>>>>>>> 1875596cd70af87c17b27b60893856cce4c85f6d
        else:
            return HttpResponse('Método no permitido', status=405)
    else:
        return HttpResponse('Acceso denegado', status=403)

@login_required
def pagos_create(request):
    role = getRole(request)
    email = get_email(request)
    
    # Verificar si el usuario es administrador o tiene el correo permitido
    if role == "Administrador de Pagos" or email == "rector@colegio.com":
        if request.method == 'POST':
            form = PagosForm(request.POST)
            if form.is_valid():
                lp.create_pagos(form)
                messages.add_message(request, messages.SUCCESS, 'Pago creado exitosamente')
                return HttpResponseRedirect(reverse('pagos_view'))
            else:
                print(form.errors)
        else:
            form = PagosForm()
        return render(request, 'pagos/pagos_create.html', {'form': form})
    else:
        return HttpResponse('Acceso denegado', status=403)
