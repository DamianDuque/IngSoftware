from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import *

# Create your views here.

usr_id = 1
usuarios_obj = Usuario.objects.get(id_usuario = usr_id)

def home(request):
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'home.html', {'name':usuarios_obj.nombre_usuario})

def Empresas(request):
    info_tablaE = Empresa.objects.filter()
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'empresas.html', {'tabla_empresas': info_tablaE, 'name':usuarios_obj.nombre_usuario})

def Aspirantes(request):
    info_tablaA = Aspirante.objects.filter()
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'aspirantes.html', {'tabla_aspirantes': info_tablaA, 'name':usuarios_obj.nombre_usuario})

def ofertas(request):
    info_tablaO = Oferta.objects.filter()
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'ofertas.html', {'tabla_ofertas': info_tablaO, 'name':usuarios_obj.nombre_usuario})
    
def Matchs(request):
    info_tablaM = Match.objects.filter()
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'matchs.html', {'tabla_matchs': info_tablaM, 'name':usuarios_obj.nombre_usuario})

def documentacionAspirante(request):
    return render(request, 'docAspirante.html')

def documentacionEmpresa(request):
    return render(request, 'docEmpresa.html')

# Comandos repositorio
# 
# Copiado:
# git clone (link repositorio)
# 
# subida:
# git add .
# git commit -m "(que se hizo en el commit)"
# branch pavas
# git push pavas 