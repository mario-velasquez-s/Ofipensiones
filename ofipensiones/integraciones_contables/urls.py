from django.urls import path
from . import views

urlpatterns = [
    path('', views.integraciones_list, name='integraciones_list'),
    path('create/', views.integracion_create, name='integracion_create'),
]
