from django.shortcuts import render

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

###Paginas admin###

def mostrarIndexAdm(request):
    return render(request, 'core/administrador/index-adm.html')

def mostrarPerfilAdm(request):
    return render(request, 'core/administrador/perfil-adm.html')

def mostrarCategoriaAdm(request):
    return render(request, 'core/administrador/categoria.html')

def mostrarAgregar(request):
    return render(request, 'core/administrador/agregar.html')

def mostrarEditarPerfilAdm(request):
    return render(request, 'core/administrador/editar-perfil-adm.html')

def mostrarCambioContraAdm(request):
    return render(request, 'core/administrador/cambiar-contrasena-adm.html')

def mostrarProductoAdm(request):
    return render(request, 'core/administrador/producto-adm.html')