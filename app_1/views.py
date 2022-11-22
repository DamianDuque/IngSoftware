from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import ingresarAspiranteForm, ingresarEmpresaForm, ingresarOfertaForm

# Create your views here.

usr_id = 2
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
    #data={
    #   'formOferta': ingresarOfertaForm()
    #}
    #if request.method == 'POST':
    #    formulario = ingresarOfertaForm(data=request.POST)
    #    if formulario.is_valid():
    #        formulario.save()
    #        data["mensaje"] = "Oferta Guardada"
    #    else:
    #        data["formOferta"] =formulario
    #        data["mensaje"] = "Syntax Error"

    formulario = ingresarOfertaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Nueva oferta publicada con éxito.")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('ofertas')

    return render(request, 'formularios/ingresarOferta.html', {'formulario': formulario})#data)

def ingresarEmpresa(request):
    #data={
    #   'formEmpresa': ingresarEmpresaForm()
    #}
    #if request.method == 'POST':
    #    formulario = ingresarEmpresaForm(data=request.POST)
    #    if formulario.is_valid():
    #        formulario.save()
    #        data["mensaje"] = "Oferta Guardada"
    #    else:
    #        data["formEmpresa"] =formulario
    #        data["mensaje"] = "Syntax Error"
    formulario = ingresarEmpresaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Nueva Empresa registrada con éxito.")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('empresas')
    return render(request, 'formularios/ingresarEmpresa.html')

def ingresarAspirante(request):
    #data={
    #   'formAspirante': ingresarAspiranteForm()
    #}
    #if request.method == 'POST':
    #    formulario = ingresarAspiranteForm(data=request.POST)
    #    if formulario.is_valid():
    #        formulario.save()
    #        data["mensaje"] = "Oferta Guardada"
    #    else:
    #        data["formAspirante"] =formulario
    #        data["mensaje"] = "Syntax Error"
    formulario = ingresarAspiranteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Nuevo Aspirante agregado con éxito.")  # prueba de funcionalidad
        #return redirect('homes')
        return redirect('aspirantes')
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