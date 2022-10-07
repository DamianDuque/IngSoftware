from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Aspirante)
admin.site.register(documentacionEmpresa)
admin.site.register(documentacionAspirante)
admin.site.register(Oferta)
admin.site.register(Match)