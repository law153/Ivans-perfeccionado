from django.urls import path,include
from .views import mostrarIndex, mostrarNosotros, mostrarRegistro,mostrarIni_sesion, mostrarOlv_contra, mostrarPregunta, mostrarProducto, mostrarCategoria, mostrarIndexAdm, mostrarPerfilAdm, mostrarCategoriaAdm, mostrarAgregar, mostrarEditarPerfilAdm, mostrarCambioContraAdm, mostrarProductoAdm, mostrarProductoCli, mostrarCategoriaCli, mostrarMetodoPago, mostrarNosotrosCli, mostrarPerfilCli, mostrarIndexCli, mostrarCarritoCli, mostrarCambioContraCli, mostrarEditarPerfilCli,registrarUsuario,consultar, agregarProducto, inicioSesion, agregarAlCarrito, consultarCli, editarProducto

urlpatterns = [

    ### Paginas sin-cuenta###
    path('',mostrarIndex,name="mostrarIndex"),
    path('nosotros/',mostrarNosotros,name="mostrarNosotros"),
    path('registro/',mostrarRegistro,name="mostrarRegistro"),
    path('iniciar_sesion/',mostrarIni_sesion,name="mostrarIni_sesion"),
    path('olvide_mi_clave/',mostrarOlv_contra,name="mostrarOlv_contra"),
    path('pregunta_de_seguridad/',mostrarPregunta,name="mostrarPregunta"),
    path('producto/<id_prod>',mostrarProducto,name="mostrarProducto"),
    path('categoria/<id_cate>',mostrarCategoria,name="mostrarCategoria"),
    path('registrarUsuario/',registrarUsuario,name='registrarUsuario'),
    path('consultar/',consultar,name="consultar"),
    path('inicioSesion/',inicioSesion, name="inicioSesion"),
    ### Paginas cliente###
    path('producto_cli/<id_prod>',mostrarProductoCli,name="mostrarProductoCli"),
    path('principal_cli/',mostrarIndexCli,name="mostrarIndexCli"),
    path('carrito_cli/',mostrarCarritoCli,name="mostrarCarritoCli"),
    path('metodo_de_pago/',mostrarMetodoPago,name="mostrarMetodoPago"),
    path('nosotros_cli/',mostrarNosotrosCli,name="mostrarNosotrosCli"),
    path('editar_perfil_cli/',mostrarEditarPerfilCli,name="mostrarEditarPerfilCli"),
    path('perfil_cli/',mostrarPerfilCli,name="mostrarPerfilCli"),
    path('cambio_de_contrasena_cli/',mostrarCambioContraCli,name="mostrarCambioContraCli"),
    path('categoria_cli/<id_cate>',mostrarCategoriaCli,name="mostrarCategoriaCli"),
    path('agregarAlCarrito/',agregarAlCarrito, name="agregarAlCarrito"),
    path('consultarCli/',consultarCli,name="consultarCli"),
    ### Paginas admin###
    path('principal_adm/',mostrarIndexAdm,name="mostrarIndexAdm"),
    path('categoria_adm/<id_cate>', mostrarCategoriaAdm, name="mostrarCategoriaAdm"),
    path('perfil_adm/',mostrarPerfilAdm, name="mostrarPerfilAdm"),
    path('agregar/', mostrarAgregar, name="mostrarAgregar"),
    path('editar_perfil_adm/', mostrarEditarPerfilAdm, name="mostrarEditarPerfilAdm"),
    path('cambio_contra_adm/', mostrarCambioContraAdm, name="mostrarCambioContraAdm"),
    path('producto_adm/<id_prod>', mostrarProductoAdm, name="mostrarProductoAdm"),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('editarProducto/', editarProducto, name="editarProducto"),

]
