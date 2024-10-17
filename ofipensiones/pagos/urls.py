from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('pagos', views.pagos_view, name='pagos_view'),
    path('pagoscreate/',csrf_exempt(views.pagos_create),name='pagosCreate')
]
