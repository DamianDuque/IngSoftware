from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Usuario'})

def Empresas(request):
    return render(request, 'empresas.html')

def Aspirantes(request):
    return render(request, 'aspirantes.html')

def ofertas(request):
    return render(request, 'ofertas.html')
    
def Matchs(request):
    return render(request, 'matchs.html')

def documentacionAspirante(request):
    return render(request, 'docAspirante.html')

def documentacionEmpresa(request):
    return render(request, 'docEmpresa.html')