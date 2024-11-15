from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.pagos_view, name='pagos_view'),
    path('create/', views.pagos_create, name='pagos_create'),
]
