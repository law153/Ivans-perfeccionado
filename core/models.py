from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, verbose_name='Solo dos posibles, 1 para cliente y 2 para admin')
    nombre_rol = models.CharField(max_length=30)

class Pregunta(models.Model):
    id_pregunta = models.IntegerField(primary_key=True, verbose_name='De momento solo 1,2 y 3')
    nombre_pregunta = models.CharField(max_length=60)

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='De momento solo 7')
    nombre_categoria = models.CharField(max_length=30)

class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    nombre_consultante = models.CharField(max_length=30)
    asunto_consulta = models.CharField(max_length=60)
    mensaje_consulta = models.CharField(max_length=200)

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


class Producto(models.Model):
    cod_prod = models.AutoField(primary_key=True)
    nombre_prod = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    stock = models.IntegerField()
    foto_prod = models.ImageField(upload_to="productos")
    unidad_medida = models.CharField(max_length=30)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    estado = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    total = models.IntegerField()
    carrito = models.BooleanField(verbose_name='0 para venta y 1 para carrito')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

###incremental: models.AutoField()###
###imagenes: foto = models.ImageField(upload_to="carpeta")###
###clave foranea: dato = models.ForeignKey(Raza,on_delete=models.CASCADE)###