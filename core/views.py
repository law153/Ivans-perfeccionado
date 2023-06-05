from django.shortcuts import render, redirect
from .models import Rol, Pregunta, Categoria, Consulta, Usuario, Producto, Venta, Detalle
from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.core.files import File
import os
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
    pregunta = Pregunta.objects.all()

    contexto = {"categorias" : categoria,
                "preguntas" : pregunta}
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

    usuario1 = Usuario.objects.get(rut = rutU)
    usuario2 = Usuario.objects.get(correo = correoU)

    if usuario1 or usuario2:
        messages.error(request,'Ya existe una cuenta con el correo/rut ingresado')
        return redirect('mostrarRegistro')
    else:
        Usuario.objects.create( rut = rutU,
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
            request.session['username'] = user1.username
            return redirect('mostrarIndexCli')
        else:
            request.session['username'] = user1.username
            return redirect('mostrarIndexAdm')
    else:
        messages.error(request,'El usuario no existe')
        return redirect('mostrarIni_sesion')
    
def cierreSesion(request):
    logout(request)
    return redirect('mostrarIndex')

def revisarDatos(request):
    rutR = request.POST['rut']
    dvrutR = request.POST['dvrut']
    idPreguntaR = request.POST['pregunta']
    respuestaR = request.POST['respuesta']


    try:    
        usuario = Usuario.objects.get(rut = rutR)
    except Usuario.DoesNotExist:
        messages.error(request,'El rut no está registrado')
        return redirect('mostrarPregunta')

    if str(usuario.dvrut) == str(dvrutR):

        preguntaR = Pregunta.objects.get(id_pregunta = idPreguntaR)
        if str(usuario.pregunta).strip().lower() == str(preguntaR).strip().lower() and str(usuario.respuesta).strip().lower() == str(respuestaR).strip().lower():
            user = User.objects.get(username = usuario.correo)
            login(request, user)
            request.session['username'] = user.username 
            return redirect('mostrarOlv_contra')
        else:
            messages.error(request,'La pregunta o respuesta no son correctas')
            return redirect('mostrarPregunta')
    else:
        messages.error(request,'El digito verificador no es correcto')
        return redirect('mostrarPregunta')
    
def olvideClave(request):
    usernameP = request.session.get('username')
    usuario = Usuario.objects.get(correo = usernameP)
    user = User.objects.get(username = usernameP)

    contraN = request.POST['contra_nueva']

    usuario.clave = contraN
    user.set_password(contraN)

    usuario.save()
    user.save()

    return redirect('cierreSesion')  
        

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

    username = request.session.get('username')
    usuario = Usuario.objects.get(correo = username)

    contexto = {
        "user" : usuario,
        "categorias" : categoria
    }

    return render(request, 'core/cliente/Perfil.html',contexto)

def mostrarIndexCli(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/cliente/index-cli.html',contexto)

def mostrarCarritoCli(request):
    categoria = Categoria.objects.all()

    username = request.session.get('username')
    usuario1 = Usuario.objects.get(correo = username)

    carrito = Venta.objects.filter(usuario = usuario1, estado='ACTIVO').first()

    if carrito:
        detalles = Detalle.objects.filter(venta = carrito)
        totalV = 0
        for i in detalles:
            totalV += i.subtotal
        carrito.total = totalV
        carrito.save()
        contexto = {"categorias" : categoria,
                    "carrito" : detalles,
                    "venta" : carrito}
        if not detalles:
            carrito.estado = 'INACTIVO'
            carrito.save()
    else:
        contexto = {"categorias" : categoria}
        messages.warning(request,'No hay productos en el carrito actualmente')
    
    return render(request, 'core/cliente/carrito.html',contexto)

def mostrarCambioContraCli(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/cliente/cambiar-contrasena-cli.html',contexto)

def mostrarEditarPerfilCli(request):
    categoria = Categoria.objects.all()

    username = request.session.get('username')

    usuario = Usuario.objects.get(correo = username)

    preguntaObjeto = Pregunta.objects.all()

    contexto = {
        "user" : usuario,
        "pregunta": preguntaObjeto,
        "categorias" : categoria
    }
    
    return render(request, 'core/cliente/Editar-perfil.html',contexto)

def editarPerfilCli(request):
    usernameP = request.session.get('username')

    nombreU = request.POST['nombre']
    apellidoU = request.POST['apellido']
    rutU = request.POST['rut']
    dvrutU = request.POST['dvrut']
    telefonoU = request.POST['telefono']
    direccionU = request.POST['direccion']
    correoU = request.POST['correo']
    idpreguntaU = request.POST['pregunta']
    respuestaU = request.POST['respuesta']

    usuario = Usuario.objects.get(correo = usernameP)
    usuario2 = User.objects.get(username = usuario.correo)

    fotoU = request.FILES.get('imagen',usuario.foto_usuario)

    if Usuario.objects.filter(rut = rutU).exclude(id_usuario = usuario.id_usuario).exists():
        messages.error(request, 'Ya existe un usuario con ese RUT.')
        return redirect('mostrarEditarPerfilCli')
    
    if Usuario.objects.filter(correo = correoU).exclude(correo = usuario.correo).exists():
        messages.error(request, 'Ya existe un usuario con ese correo.')
        return redirect('mostrarEditarPerfilCli')

    usuario.rut = rutU
    usuario.dvrut = dvrutU
    usuario.nombre = nombreU
    usuario.apellido = apellidoU
    usuario.telefono = telefonoU
    usuario.correo = correoU
    usuario.direccion = direccionU
    usuario.respuesta = respuestaU
    usuario.foto_usuario = fotoU
    registroPregunta = Pregunta.objects.get(id_pregunta = idpreguntaU)
    usuario.pregunta = registroPregunta

    usuario2.username = correoU
    usuario2.email = correoU

    usuario.save()
    usuario2.save()

    messages.success(request,'Perfil editado correctamente (o no cambió nada)')        
    return redirect('mostrarPerfilCli')

def eliminarCuenta(request,id_user):
    usuario = Usuario.objects.get(id_usuario = id_user)
    user = User.objects.get(username = usuario.correo)
    usuario.delete()
    user.delete()

    messages.success(request,'Cuenta borrada exitosamente')
    return redirect('mostrarIndex')

def agregarAlCarrito(request):

    cod_produc = request.POST['id_product']
    productoC = Producto.objects.get(cod_prod = cod_produc)

    username = request.session.get('username')
    usuarioC = Usuario.objects.get(correo = username)
    
    fecha_hoy = date.today()
    entrega = timedelta(999)
    fecha_e = fecha_hoy + entrega


    carrito = Venta.objects.filter(usuario = usuarioC, estado='ACTIVO').first()

    if carrito:
        detalle = Detalle.objects.get(venta = carrito, producto = productoC)
        if detalle:
            detalle.cantidad += 1
            detalle.subtotal += productoC.precio
            detalle.save()

            
        else:
            Detalle.objects.create(cantidad = 1,
                                    subtotal = productoC.precio,
                                    venta = carrito,
                                    producto = productoC)


    else:
        carrito = Venta.objects.create(fecha_venta = fecha_hoy,
                                       estado = "ACTIVO",
                                       fecha_entrega = fecha_e,
                                       total = productoC.precio,
                                       carrito = 1,
                                       usuario = usuarioC)

        Detalle.objects.create(cantidad = 1,
                                subtotal = productoC.precio,
                                venta = carrito,
                                producto = productoC)
        
    return redirect('mostrarCarritoCli')

def sacarDelCarro(request, cod_detalle):
    detalle = Detalle.objects.get(id_detalle = cod_detalle)
    detalle.delete()
    

    return redirect('mostrarCarritoCli')

def cambiarCantidad(request, cod_detalle):
    detalle = Detalle.objects.get(id_detalle = cod_detalle)
    cant = int(request.POST['nueva_cantidad_{}'.format(cod_detalle)])

    cantidadC = int(cant)

    if cantidadC >= 0:
        detalle.cantidad = cantidadC
        detalle.subtotal = detalle.producto.precio * cantidadC
        detalle.save()
        return redirect('mostrarCarritoCli')
    else:
        messages.warning(request,'La cantidad no puede ser menor a 1')
        return redirect('mostrarCarritoCli')
    
def pagarCarrito(request):

    username = request.session.get('username')
    usuarioC = Usuario.objects.get(correo = username)
    
    carritoP = Venta.objects.filter(usuario = usuarioC, estado='ACTIVO').first()

    carritoP.estado = 'PAGANDO'

    carritoP.carrito = 0

    carritoP.save()

    messages.warning(request,'Esta función no está implementada')
    return redirect('mostrarError')


def consultarCli(request):
    
    username = request.session.get('username')
    usuario = Usuario.objects.get(correo = username)


    asuntoC = request.POST['asunto']
    mensajeC = request.POST['msg']

    Consulta.objects.create(nombre_consultante = usuario.nombre,
                            asunto_consulta = asuntoC,
                            mensaje_consulta = mensajeC)
    return redirect('mostrarNosotrosCli')


def cambiarClaveCli(request):

    usernameP = request.session.get('username')
    contraA = request.POST['contra_actual']
    contraN = request.POST['contra_nueva']

    usuario = Usuario.objects.get(correo = usernameP)
    usuario2 = User.objects.get(username = usuario.correo)
    if str(usuario.clave) == str(contraA):

        usuario.clave = contraN
        usuario2.set_password(contraN)

        usuario.save()
        usuario2.save()
        messages.success(request,'Contraseña cambiada correctamente')
        return redirect('mostrarPerfilCli')

    else:
        messages.error(request,'La contraseña actual es incorrecta')
        return redirect('mostrarCambioContraCli')
    

###Paginas admin###

def mostrarIndexAdm(request):
    categoria = Categoria.objects.all()
    
    contexto = {"categorias" : categoria}
    return render(request, 'core/administrador/index-adm.html',contexto)

def mostrarPerfilAdm(request):
    categoria = Categoria.objects.all()

    username = request.session.get('username')
    usuario = Usuario.objects.get(correo = username)

    contexto = {
        "user" : usuario,
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

    username = request.session.get('username')
    usuario = Usuario.objects.get(correo = username)

    preguntaObjeto = Pregunta.objects.all()

    contexto = {
        "user" : usuario,
        "pregunta": preguntaObjeto,
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

def mostrarEditarRol(request):
    categoria = Categoria.objects.all()
    clientes = Usuario.objects.all()

    contexto = {
        "clients": clientes,
        "categorias": categoria
    }
    return render(request, 'core/administrador/Editar-rol.html',contexto)

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
    messages.success(request,'El producto fue agregado correctamente')
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
    messages.success(request,'El producto fue editado correctamente')
    
    return redirect('mostrarIndexAdm')

def eliminarProducto(request,id_prod):
    producto = Producto.objects.get(cod_prod = id_prod)
    producto.delete()
    messages.error(request,'Producto eliminado')
    return redirect('mostrarIndexAdm')

def editarPerfilAdm(request):
    usernameP = request.session.get('username')

    nombreU = request.POST['nombre']
    apellidoU = request.POST['apellido']
    rutU = request.POST['rut']
    dvrutU = request.POST['dvrut']
    telefonoU = request.POST['telefono']
    direccionU = request.POST['direccion']
    correoU = request.POST['correo']
    idpreguntaU = request.POST['pregunta']
    respuestaU = request.POST['respuesta']

    usuario = Usuario.objects.get(correo = usernameP)
    usuario2 = User.objects.get(username = usuario.correo)

    fotoU = request.FILES.get('imagen',usuario.foto_usuario)

    if Usuario.objects.filter(rut = rutU).exclude(id_usuario = usuario.id_usuario).exists():
        messages.error(request, 'Ya existe un usuario con ese RUT.')
        return redirect('mostrarEditarPerfilAdm')
    
    if Usuario.objects.filter(correo = correoU).exclude(correo = usuario.correo).exists():
        messages.error(request, 'Ya existe un usuario con ese correo.')
        return redirect('mostrarEditarPerfilAdm')

    usuario.rut = rutU
    usuario.dvrut = dvrutU
    usuario.nombre = nombreU
    usuario.apellido = apellidoU
    usuario.telefono = telefonoU
    usuario.correo = correoU
    usuario.direccion = direccionU
    usuario.respuesta = respuestaU
    usuario.foto_usuario = fotoU
    registroPregunta = Pregunta.objects.get(id_pregunta = idpreguntaU)
    usuario.pregunta = registroPregunta

    usuario2.username = correoU
    usuario2.email = correoU

    usuario.save()
    usuario2.save()
    messages.success(request,'Perfil editado correctamente (o no cambió nada)')
    
    return redirect('mostrarPerfilAdm')

def cambiarClaveAdm(request):

    usernameP = request.session.get('username')
    contraA = request.POST['contra_actual']
    contraN = request.POST['contra_nueva']

    usuario = Usuario.objects.get(correo = usernameP)
    usuario2 = User.objects.get(username = usuario.correo)

    if str(usuario.clave) == str(contraA):

        usuario.clave = contraN
        usuario2.set_password(contraN)
        usuario.save()
        usuario2.save()
        messages.success(request,'Contraseña cambiada correctamente')
        return redirect('mostrarPerfilAdm')

    else:
        messages.error(request,'La contraseña actual es incorrecta')
        return redirect('mostrarCambioContraAdm')

def editarRol(request,id):
    usuario = Usuario.objects.get(id_usuario = id)
    usuario2 = User.objects.get(username = usuario.correo)

    if usuario.rol.id_rol == 1:
        registrolRol = Rol.objects.get(id_rol = 2)
        usuario.rol = registrolRol
        usuario2.is_staff = True
    else:
        registrolRol = Rol.objects.get(id_rol = 1)
        usuario.rol = registrolRol
        usuario2.is_staff = False
    
    usuario.save()
    usuario2.save()
    messages.success(request,"Rol cambiado con éxito")
    return redirect('mostrarEditarRol')    
    


