from django import forms
from .models import Aspirante, Empresa, Oferta

class ingresarOfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        #fields = ["Empresa_id_empresa", "Nombre_empresa", "cargo", "perfil_buscado", "salario"]
        fields = '__all__'

class ingresarEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class ingresarAspiranteForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = '__all__'