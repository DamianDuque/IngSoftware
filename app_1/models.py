from django.db import models
# Create your models here.


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, blank=False)
    nombre_usuario = models.CharField(max_length=45, null=False)
    contrasena_usuario = models.CharField(max_length=45, null=False)
    tipo_usuario = models.CharField(max_length=45, null=False, choices=(('Empresa','Empresa'),('Aspirante', 'Aspirante')))


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True, blank=False)
    Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
    nombre_empresa = models.CharField(max_length=45, null=False)
    correo_empresa = models.CharField(max_length=45, null=False)
    presentacion_empresa = models.CharField(max_length=1000, null=False)
    nit = models.CharField(max_length=45, null=False)
    sectorEconomico = models.CharField(max_length=45, null=False, choices=(('Primario','Primario'),('Secundario', 'Secundario'),('Terciario','Terciario'),('Cuaternario','Cuaternario')))


class Aspirante(models.Model):
    id_aspirante = models.AutoField(primary_key=True, blank=False)
    Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
    nombre_aspirante = models.CharField(max_length=45, null=False)
    correo_aspirante = models.CharField(max_length=45, null=False)
    presentacion_aspirante = models.CharField(max_length=1000, null=False)
    cedulaciudadania = models.PositiveIntegerField(default=0)
    certificaciones = models.CharField(max_length=200, null=False)
    experiencia = models.CharField(max_length=1000, null=False)
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)


class documentacionEmpresa(models.Model):
    Empresa_id_empresa = models.ForeignKey(Empresa, null= False, blank=False, on_delete=models.CASCADE)
    politicas = models.CharField(max_length=1000, null=False)
    tyc = models.CharField(max_length=1000, null=False)


class documentacionAspirante(models.Model):
    Aspirante_id_aspirante = models.ForeignKey(Aspirante, null= False, blank=False, on_delete=models.CASCADE)
    hdv = models.CharField(max_length=1000, null=False)
    recomendaciones = models.CharField(max_length=1000, null=False)


class Oferta(models.Model):
    id_Oferta = models.AutoField(primary_key=True, blank=False)
    Empresa_id_empresa = models.ForeignKey(Empresa, null= False, blank=False, on_delete=models.CASCADE)
    Nombre_empresa = models.CharField(max_length=45, null=True)
    cargo = models.CharField(max_length=45, null=False)
    perfil_buscado = models.CharField(max_length=200, null=False)
    salario = models.PositiveIntegerField(default=0)


class Match(models.Model):
    Oferta_id_oferta = models.ForeignKey(Oferta, null= False, blank=False, on_delete=models.CASCADE)
    Empresa_id_empresa = models.ForeignKey(Empresa, null= False, blank=False, on_delete=models.CASCADE)
    Aspirante_id_aspirante = models.ForeignKey(Aspirante, null= False, blank=False, on_delete=models.CASCADE)
    Nombre_empresa = models.CharField(max_length=45, null=True)
    fecha_match = models.DateTimeField(auto_now_add=True)
    tipo_match = models.CharField(max_length=45, null=False, choices=(('Perfecto','Perfecto'),('Muy bueno', 'Muy bueno'),('Bueno','Bueno'),('Medio','Medio')))
    porcentaje = models.PositiveIntegerField(default=0)


#python manage.py makemigrations
#python manage.py sqlmigrate app_1 0001
#python manage.py migrate

#python manage.py shell
#from app_1.models import Usuarios
#usr5 = Usuarios(codigo = 'AAA000', nombre = 'Esteban Trujillo', cantidadRecogida = 25)
