import imp
from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import *
from .forms import ingresarOfertaForm

# Create your views here.

usr_id = 1
usuarios_obj = Usuario.objects.get(id_usuario = usr_id)

def home(request):
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'home.html', {'name':usuarios_obj.nombre_usuario})

def homes(request):
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'homes.html', {'name':usuarios_obj.nombre_usuario})

def empresas(request): #cambios de mayusculas, homes es para pruebas
    info_tablaE = Empresa.objects.filter()
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'empresas.html', {'tabla_empresas': info_tablaE, 'name':usuarios_obj.nombre_usuario})

def aspirantes(request):
    info_tablaA = Aspirante.objects.filter()
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'aspirantes.html', {'tabla_aspirantes': info_tablaA, 'name':usuarios_obj.nombre_usuario})

def ofertas(request):
    info_tablaO = Oferta.objects.filter()
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'ofertas.html', {'tabla_ofertas': info_tablaO, 'name':usuarios_obj.nombre_usuario})
    
def matchs(request):
    info_tablaM = Match.objects.filter()
    usuarios_obj = Usuario.objects.get(id_usuario = usr_id)
    return render(request, 'matchs.html', {'tabla_matchs': info_tablaM, 'name':usuarios_obj.nombre_usuario})

def documentacionAspirante(request):
    return render(request, 'docAspirante.html')

def documentacionEmpresa(request):
    return render(request, 'docEmpresa.html')

def ingresarOferta(request):
    data={
       'form': ingresarOfertaForm()
    }
    if request.method == 'POST':
        formulario = ingresarOfertaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Oferta Guardada"
        else:
            data["form"] =formulario
            data["mensaje"] = "Syntax Error"
    return render(request, 'formularios/ingresarOferta.html', data)

def ingresarEmpresa(request):
    return render(request, 'formularios/ingresarEmpresa.html')

def ingresarAspirante(request):
    return render(request, 'formularios/ingresarAspirante.html')

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