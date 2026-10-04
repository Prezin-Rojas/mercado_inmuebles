from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='indice'),
    path('cuenta/', include('django.contrib.auth.urls')),
    path('cuenta/registro/', views.registro, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('act_perfil/', views.act_perfil, name='act_perfil'),
    path('inmuebles/nuevo/' , views.nuevo_inmueble, name='nuevo_inmueble'),
    path('inmuebles/<int:id>/actualizar', views.act_inmueble, name='actualizar_inmueble'),
    path('inmuebles/<int:id>/borrar', views.borrar_inmueble, name='borrar_inmueble'),
]