from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
]
