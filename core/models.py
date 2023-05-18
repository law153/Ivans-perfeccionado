from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, verbose_name='Solo dos posibles, 1 para cliente y 2 para admin')
    nombre_rol = models.CharField(max_length=30)

class Pregunta(models.Model):
    id_pregunta = models.IntegerField(primary_key=True, verbose_name='De momento solo 1,2 y 3')
    nombre_pregunta = models.CharField(max_length=60)

class categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='De momento solo 7')
    nombre_categoria = models.CharField(max_length=30)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut = models.IntegerField()
    dvrut = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=60)
    clave = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)
    respuesta = models.CharField(max_length=50)
    foto_usuario = models.ImageField(upload_to="usuarios")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)



###incremental: models.AutoField()###
###imagenes: foto = models.ImageField(upload_to="carpeta")###
###clave foranea: dato = models.ForeignKey(Raza,on_delete=models.CASCADE)###