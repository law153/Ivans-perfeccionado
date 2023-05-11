from django.shortcuts import render

# Create your views here.
def mostrarIndex(request):
    return render(request, 'core/index.html')

def mostrarNosotros(request):
    return render(request, 'core/sin-cuenta/nosotros.html')

def mostrarRegistro(request):
    return render(request, 'core/sin-cuenta/registrarse.html')

def mostrarIni_sesion(request):
    return render(request, 'core/sin-cuenta/inicio-sesion.html')

def mostrarOlv_contra(request):
    return render(request, 'core/sin-cuenta/olvidar-contraseña.html')

def mostrarPregunta(request):
    return render(request, 'core/sin-cuenta/Pregunta.html')

def mostrarProducto(request):
    return render(request, 'core/sin-cuenta/Producto.html')

def mostrarCategoria(request):
    return render(request, 'core/sin-cuenta/Categoria.html')

def mostrarNosotros(request):
    return render(request, 'core/sin-cuenta/nosotros.html')