from pyexpat import model
from socket import fromshare
from django import forms
from .models import Oferta

class ingresarOfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ["Empresa_id_empresa", "Nombre_empresa", "cargo", "perfil_buscado", "salario"]
        #fields = '__all__'