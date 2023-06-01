from django.shortcuts import render, redirect
from .models import Rol, Pregunta, Categoria, Consulta, Usuario, Producto, Venta, Detalle
from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
# Create your views here.

###Paginas sin-cuenta###
def mostrarIndex(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}

    return render(request, 'core/index.html',contexto)

def mostrarError(request):
    return render(request, 'core/error.html')

def mostrarNosotros(request):
    categoria = Categoria.objects.all()

    contexto = {"categorias" : categoria}

    return render(request, 'core/sin-cuenta/nosotros.html',contexto)

def mostrarRegistro(request):
    categoria = Categoria.objects.all()

    contexto = {"categorias" : categoria}

    return render(request, 'core/sin-cuenta/registrarse.html',contexto)

def mostrarIni_sesion(request):
    categoria = Categoria.objects.all()

    contexto = {"categorias" : categoria}

    return render(request, 'core/sin-cuenta/inicio-sesion.html',contexto)

def mostrarOlv_contra(request):
    categoria = Categoria.objects.all()

    contexto = {"categorias" : categoria}
    return render(request, 'core/sin-cuenta/olvidar-contrasena.html',contexto)

def mostrarPregunta(request):
    categoria = Categoria.objects.all()

    contexto = {"categorias" : categoria}
    return render(request, 'core/sin-cuenta/Pregunta.html',contexto)

def mostrarProducto(request, id_prod):
    categoria = Categoria.objects.all() 

    producto = Producto.objects.get(cod_prod = id_prod)
    
    contexto = {"product" : producto, "categorias" : categoria}

    return render(request, 'core/sin-cuenta/Producto.html',contexto)

def mostrarCategoria(request, id_cate):
    categoria = Categoria.objects.all()

    cate = Categoria.objects.get(id_categoria = id_cate)

    productos = Producto.objects.filter(categoria = cate)
    
    contexto = {"products" : productos ,"categorias" : categoria, "categoria" : cate}

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
    
    user = User.objects.create_user(username = correoU, email = correoU, password = claveU )
    user.is_staff = False
    user.is_active = True
    user.save()

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

    try:
        user1 = User.objects.get(username = correoI)
    except User.DoesNotExist:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect('mostrarIni_sesion')
    
    pass_valida = check_password(claveI, user1.password)
    if not pass_valida:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect('mostrarIni_sesion')
    usuario = Usuario.objects.get(correo = correoI, clave = claveI)
    user = authenticate(username = correoI, password = claveI)
    if user is not None:
        login(request, user)
        if(usuario.rol.id_rol == 1):
            return redirect('mostrarIndexCli')
        else:
            return redirect('mostrarIndexAdm')
    else:
        messages.error(request,'El usuario no existe')
        return redirect('mostrarIni_sesion')
    
def cierreSesion(request):
    logout(request)
    redirect('mostrarIndex')

###Paginas cliente###
def mostrarProductoCli(request, id_prod):
    categoria = Categoria.objects.all() 

    producto = Producto.objects.get(cod_prod = id_prod)
    
    contexto = {"product" : producto, "categorias" : categoria}

    return render(request, 'core/cliente/Producto-cli.html',contexto)

def mostrarCategoriaCli(request, id_cate):
    categoria = Categoria.objects.all()

    cate = Categoria.objects.get(id_categoria = id_cate)

    productos = Producto.objects.filter(categoria = cate)
    
    contexto = {"products" : productos ,"categorias" : categoria, "categoria" : cate}

    return render(request, 'core/cliente/Categoria-cli.html', contexto)

def mostrarMetodoPago(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/cliente/Metodo-pago.html',contexto)

def mostrarNosotrosCli(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/cliente/nosotros-cli.html',contexto)

def mostrarPerfilCli(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/cliente/Perfil.html',contexto)

def mostrarIndexCli(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/cliente/index-cli.html',contexto)

def mostrarCarritoCli(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/cliente/carrito.html',contexto)

def mostrarCambioContraCli(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/cliente/cambiar-contrasena-cli.html',contexto)

def mostrarEditarPerfilCli(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}

    return render(request, 'core/cliente/Editar-perfil.html',contexto)

def agregarAlCarrito(request):

    cod_produc = request.POST['id_product']
    productoC = Producto.objects.get(cod_prod = cod_produc)

    id_user = 1
    usuarioC = Usuario.objects.get(id_usuario = id_user)
    
    fecha_hoy = date.today()
    entrega = timedelta(3)

    fecha_e = fecha_hoy + entrega

    ventaC = Venta.objects.create(
        fecha_venta = fecha_hoy,
        estado = 'En proceso',
        fecha_entrega = fecha_e,
        total = productoC.precio,
        carrito = 1,
        usuario = usuarioC
    )

    Detalle.objects.create(
        cantidad = 1,
        subtotal = productoC.precio,
        venta = ventaC,
        producto = productoC
    )

    return redirect('mostrarCarritoCli')

def consultarCli(request):
    
    nombreC = request.POST['nom-ap']
    asuntoC = request.POST['asunto']
    mensajeC = request.POST['msg']

    Consulta.objects.create(nombre_consultante = nombreC,
                            asunto_consulta = asuntoC,
                            mensaje_consulta = mensajeC)
    return redirect('mostrarNosotrosCli')

###Paginas admin###

def mostrarIndexAdm(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/administrador/index-adm.html',contexto)

def mostrarPerfilAdm(request):
    categoria = Categoria.objects.all()

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
        "categorias" : categoria
    }

    return render(request, 'core/administrador/perfil-adm.html',contexto)

def mostrarCategoriaAdm(request, id_cate):
    categoria = Categoria.objects.all()

    cate = Categoria.objects.get(id_categoria = id_cate)

    productos = Producto.objects.filter(categoria = cate)
    
    contexto = {"products" : productos ,"categorias" : categoria, "categoria" : cate}

    return render(request, 'core/administrador/categoria-adm.html',contexto)

def mostrarAgregar(request):

    categories = Categoria.objects.all()
    contexto = {
        "categorias" : categories
    }
    return render(request, 'core/administrador/Agregar.html',contexto)

def mostrarEditarPerfilAdm(request):
    categoria = Categoria.objects.all()
    

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
        "respuesta": respuestaPerfil,
        "categorias" : categoria
    }
    
    return render(request, 'core/administrador/Editar-perfil-adm.html',contexto)

def mostrarCambioContraAdm(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/administrador/cambiar-contrasena-adm.html',contexto)

def mostrarProductoAdm(request,id_prod):
    categoria = Categoria.objects.all() 

    producto = Producto.objects.get(cod_prod = id_prod)
    
    contexto = {
        "product" : producto,
        "categorias" : categoria
    }

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

    Producto.objects.create(nombre_prod = nombreP, descripcion = descripcionP, precio = precioP, stock = stockP, foto_prod = fotoP, unidad_medida = unidadP, categoria = registroCategoria)
    return redirect('mostrarAgregar')

def editarProducto(request):
    codigoP = request.POST['id']
    nombreP = request.POST['nombre']
    descripcionP = request.POST['descripcion']
    precioP = request.POST['precio']
    stockP = request.POST['stock']
    fotoP = request.FILES['imagen']
    unidadP = request.POST['medida']
    categoriaP = request.POST['categoria']

    producto = Producto.objects.get(cod_prod = codigoP)
    producto.nombre_prod = nombreP
    producto.descripcion = descripcionP
    producto.precio = precioP
    producto.stock = stockP
    producto.foto_prod = fotoP
    producto.unidad_medida = unidadP

    registroCategoria = Categoria.objects.get(id_categoria = categoriaP)
    producto.categoria = registroCategoria
    producto.save()
    
    return redirect('mostrarIndexAdm')




