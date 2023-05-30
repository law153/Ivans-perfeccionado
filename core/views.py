from django.shortcuts import render, redirect
from .models import Rol, Pregunta, Categoria, Consulta, Usuario, Producto, Venta, Detalle
from datetime import date, timedelta
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

def mostrarProducto(request, id_prod):
    producto = Producto.objects.get(cod_prod = id_prod)

    contexto = {"product" : producto}

    return render(request, 'core/sin-cuenta/Producto.html',contexto)

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
def mostrarProductoCli(request, id_prod):
    producto = Producto.objects.get(cod_prod = id_prod)

    contexto = {"product" : producto}

    return render(request, 'core/cliente/Producto-cli.html',contexto)

def mostrarCategoriaCli(request):
    productos = Producto.objects.all()
    
    contexto = {"products" : productos}

    return render(request, 'core/cliente/Categoria-cli.html', contexto)

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

def agregarAlCarrito(request):

    cod_produc = 1
    
    fecha_hoy = date.today()
    dias = timedelta(3)

    fecha_e = fecha_hoy + dias

    usuario_id = 1

    productoC = Producto.objects.get(cod_prod = cod_produc)

    precioP = productoC.precio

    UsuarioC = Usuario.objects.get(id_usuario = usuario_id)

    Venta.objects.create(
        fecha_venta = fecha_hoy,
        estado = 'Agregado',
        fecha_entrega = fecha_e,
        total = precioP,
        carrito = 1,
        usuario = UsuarioC
    )

    ventaC = Venta.objects.get(id_venta = 2)

    Detalle.objects.create(
        cantidad = 1,
        subtotal = precioP,
        venta = ventaC,
        producto = productoC
    )

    return redirect('mostrarCarritoCli')

###Paginas admin###

def mostrarIndexAdm(request):
    return render(request, 'core/administrador/index-adm.html')

def mostrarPerfilAdm(request):
    nombrePerfil = "Abelardo"
    apellidoPerfil = "Sánchez"
    rutPerfil = 21342568
    dvrutPerfil = 4
    telefonoPerfil = 64982253
    direccionPerfil = "Caupolicán 1257"

    contexto = {
        "nombre": nombrePerfil,
        "apellido": apellidoPerfil,
        "rut": rutPerfil,
        "dvrut": dvrutPerfil,
        "telefono": telefonoPerfil,
        "direccion": direccionPerfil,
    }

    return render(request, 'core/administrador/perfil-adm.html',contexto)

def mostrarCategoriaAdm(request):
    productos = Producto.objects.all()
    
    contexto = {"products" : productos}

    return render(request, 'core/administrador/categoria-adm.html',contexto)

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
    telefonoPerfil = 64982253
    direccionPerfil = "Caupolicán 1257"
    correoPerfil = "abelx3678@gmail.com"
    preguntaObjeto = Pregunta.objects.all()
    respuestaPerfil = "Sr Papu"

    contexto = {
        "nombre": nombrePerfil,
        "apellido": apellidoPerfil,
        "rut": rutPerfil,
        "dvrut": dvrutPerfil,
        "telefono": telefonoPerfil,
        "direccion": direccionPerfil,
        "correo": correoPerfil,
        "pregunta": preguntaObjeto,
        "respuesta": respuestaPerfil
    }
    
    return render(request, 'core/administrador/Editar-perfil-adm.html',contexto)

def mostrarCambioContraAdm(request):
    return render(request, 'core/administrador/cambiar-contrasena-adm.html')

def mostrarProductoAdm(request,id_prod):
    producto = Producto.objects.get(cod_prod = id_prod)

    contexto = {"product" : producto}

    return render(request, 'core/administrador/producto-adm.html',contexto)

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



