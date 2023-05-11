from django.urls import path,include
from .views import mostrarIndex, mostrarNosotros, mostrarRegistro, mostrarIni_sesion, mostrarOlv_contra, mostrarPregunta, mostrarProducto, mostrarCategoria, mostrarIndexAdm

urlpatterns = [

    ### Paginas sin-cuenta###
    path('',mostrarIndex,name="mostrarIndex"),
    path('nosotros/',mostrarNosotros,name="mostrarNosotros"),
    path('registro/',mostrarRegistro,name="mostrarRegistro"),
    path('iniciar_sesion/',mostrarIni_sesion,name="mostrarIni_sesion"),
    path('olvide_mi_clave/',mostrarOlv_contra,name="mostrarOlv_contra"),
    path('pregunta_de_seguridad/',mostrarPregunta,name="mostrarPregunta"),
    path('producto/',mostrarProducto,name="mostrarProducto"),
    path('categoria/',mostrarCategoria,name="mostrarCategoria"),
    ### Paginas cliente###

    ### Paginas admin###
    path('principal/',mostrarIndexAdm,name="mostrarIndexAdm"),
]
