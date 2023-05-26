from django.shortcuts import render, redirect
from .models import Rol, Pregunta, Categoria, Producto

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
    return render(request, 'core/sin-cuenta/Categoria.html')

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
    return render(request, 'core/administrador/agregar.html',contexto)

def mostrarEditarPerfilAdm(request):
    return render(request, 'core/administrador/editar-perfil-adm.html')

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

    Producto.objects.create(nombre_prod = nombreP, descripcion = descripcionP, precio = precioP, stock = stockP, foto_prod = fotoP, unidad_medida = unidadP, categoria = registroCategoria)
    return redirect('mostrarAgregar')



