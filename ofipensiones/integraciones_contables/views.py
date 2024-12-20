from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import IntegracionContableForm
from .logic import logic_integraciones as li
from ofipensiones.auth0backend import getRole

@login_required
def integraciones_list(request):
    role = getRole(request)
    if role in ["Administrador Contable", "Usuario Paz y Salvo"]:
        integraciones = li.get_integraciones()
        context = {'integraciones_list': integraciones}
        return render(request, 'integraciones_contables/integraciones_list.html', context)
    else:
        return HttpResponse('Acceso denegado', status=403)

@login_required
def integracion_create(request):
    role = getRole(request)
    if role == "Administrador Contable":
        if request.method == 'POST':
            form = IntegracionContableForm(request.POST)
            if form.is_valid():
                li.create_integracion(form)
                messages.success(request, 'Integración creada exitosamente')
                return HttpResponseRedirect(reverse('integraciones_list'))
            else:
                print(form.errors)
        else:
            form = IntegracionContableForm()
        return render(request, 'integraciones_contables/integracion_create.html', {'form': form})
    else:
        return HttpResponse('Acceso denegado', status=403)
