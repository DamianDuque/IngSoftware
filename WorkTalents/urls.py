"""WorkTalents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_1 import views as vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', vistas.home, name= 'home'),
    path('', vistas.homes, name = 'homes'),
    path('aspirantes', vistas.aspirantes, name= 'aspirantes'),
    path('empresas', vistas.empresas, name= 'empresas'),
    path('ofertas', vistas.ofertas, name= 'ofertas'),
    path('matchs', vistas.matchs, name= 'matchs'),
    path('docEmpresa', vistas.documentacionEmpresa, name= 'docEmpresa'),
    path('docAspirante', vistas.documentacionAspirante, name= 'docAspirante'),

    path('ingresarOferta', vistas.ingresarOferta, name = 'ingresarOferta'),
    path('ingresarEmpresa', vistas.ingresarEmpresa, name = 'ingresarEmpresa'),
    path('ingresarAspirante', vistas.ingresarAspirante, name = 'ingresarAspirante'),
]
