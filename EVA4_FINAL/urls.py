"""
URL configuration for EVA4_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ReservasAPP.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('reservas', reservas, name='reservas'),
    path('agregarReserva', agregarReserva, name='agregarReserva'),
    path('eliminarReserva/<int:id>', eliminarReserva, name='eliminarReserva'),
    path('editarReserva/<int:id>', editarReserva, name='editarReserva'),
    path('reservasAPI', reservas_list, name='reservasAPI'),
    path('reservasAPI/<int:pk>', reservas_detail, name='reservasAPI'),
]
