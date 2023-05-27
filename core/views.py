from django.shortcuts import render, redirect
from .models import Rol, Pregunta, Categoria, Consulta, Usuario, Producto, Venta, Detalle

# Create your views here.

###Paginas sin-cuenta###
def mostrarIndex(request):
    return render(request, 'core/index.html')

def mostrarNosotros(request):
    return render(request, 'core/sin-cuenta/nosotros.html')

def mostrarRegistro(request):
    return render(request, 'core/sin-cuenta/registrarse.html')

def mostrarIni_sesion(request):
    return render(request, 'core/sin-cuenta/inicio-sesion.html')

def mostrarOlv_contra(request):
    return render(request, 'core/sin-cuenta/olvidar-contrasena.html')

def mostrarPregunta(request):
    return render(request, 'core/sin-cuenta/Pregunta.html')

def mostrarProducto(request):
    return render(request, 'core/sin-cuenta/Producto.html')

def mostrarCategoria(request):
    productos = Producto.objects.all()
    
    contexto = {"products" : productos}

    return render(request, 'core/sin-cuenta/Categoria.html',contexto)

def registrarUsuario(request):
    rutU = request.POST['rut']
    dvrutU = request.POST['dvrut']
    nombreU = request.POST['nombre']
    apellidoU = request.POST['apellido']
    telefonoU = request.POST['fono']
    direccionU = request.POST['direc']
    correoU = request.POST['correo_reg']
    claveU = request.POST['contra_ini']
    respuestaU = ' '
    registroRol = Rol.objects.get(id_rol = 1) ##Los usuarios registrados son clientes
    registroPregunta = Pregunta.objects.get(id_pregunta = 1) ##Pregunta asiganada por defecto

    Usuario.objects.create(rut = rutU,
                            dvrut = dvrutU,
                            nombre = nombreU,
                            apellido = apellidoU,
                            telefono = telefonoU,
                            correo = correoU,
                            clave = claveU,
                            direccion = direccionU,
                            respuesta = respuestaU,
                            rol = registroRol,
                            pregunta = registroPregunta)
    
    return redirect('mostrarIni_sesion')

def consultar(request):
    nombreC = request.POST['nom-ap']
    asuntoC = request.POST['asunto']
    mensajeC = request.POST['msg']

    Consulta.objects.create(nombre_consultante = nombreC,
                            asunto_consulta = asuntoC,
                            mensaje_consulta = mensajeC)
    return redirect('mostrarNosotros')

def inicioSesion(request):

    correoI = request.POST['correo_ini']
    claveI = request.POST['contra_ini']

    datos = Usuario.objects.all()

    for i in datos:

        if (i.correo == correoI and i.clave == claveI ):
            return redirect('mostrarIndexCli')
        else:
            return redirect('mostrarIni_sesion')

###Paginas cliente###
def mostrarProductoCli(request):
    return render(request, 'core/cliente/Producto-cli.html')

def mostrarCategoriaCli(request):
    return render(request, 'core/cliente/Categoria-cli.html')

def mostrarMetodoPago(request):
    return render(request, 'core/cliente/Metodo-pago.html')

def mostrarNosotrosCli(request):
    return render(request, 'core/cliente/nosotros-cli.html')

def mostrarPerfilCli(request):
    return render(request, 'core/cliente/Perfil.html')

def mostrarIndexCli(request):
    return render(request, 'core/cliente/index-cli.html')

def mostrarCarritoCli(request):
    return render(request, 'core/cliente/carrito.html')

def mostrarCambioContraCli(request):
    return render(request, 'core/cliente/cambiar-contrasena-cli.html')

def mostrarEditarPerfilCli(request):
    return render(request, 'core/cliente/Editar-perfil.html')

###Paginas admin###

def mostrarIndexAdm(request):
    return render(request, 'core/administrador/index-adm.html')

def mostrarPerfilAdm(request):
    return render(request, 'core/administrador/perfil-adm.html')

def mostrarCategoriaAdm(request):
    return render(request, 'core/administrador/categoria-adm.html')

def mostrarAgregar(request):
    categorias = Categoria.objects.all()
    contexto = {
        "categories" : categorias
    }
    return render(request, 'core/administrador/Agregar.html',contexto)

def mostrarEditarPerfilAdm(request):
    nombrePerfil = "Abelardo"
    apellidoPerfil = "Sánchez"
    rutPerfil = 21342568
    dvrutPerfil = 4
    telefonoPerfil = 964982253
    direccionPerfil = "Caupolicán 1257"

    contexto = {
        "nombre": nombrePerfil,
        "apellido": apellidoPerfil,
        "rut": rutPerfil,
        "dvrut": dvrutPerfil,
        "telefono": telefonoPerfil,
        "direccion": direccionPerfil
    }

    return render(request, 'core/administrador/perfil-adm.html',contexto)

def mostrarCambioContraAdm(request):
    return render(request, 'core/administrador/cambiar-contrasena-adm.html')

def mostrarProductoAdm(request):
    return render(request, 'core/administrador/producto-adm.html')

def agregarProducto(request):
    nombreP = request.POST['nombre']
    descripcionP = request.POST['descripcion']
    precioP = request.POST['precio']
    stockP = request.POST['stock']
    fotoP = request.FILES['imagen']
    unidadP = request.POST['medida']
    categoriaP = request.POST['categoria']

    registroCategoria = Categoria.objects.get(id_categoria = categoriaP)

    Producto.objects.create(foto_prod = fotoP, nombre_prod = nombreP, descripcion = descripcionP, precio = precioP, stock = stockP, unidad_medida = unidadP, categoria = registroCategoria)
    return redirect('mostrarAgregar')



