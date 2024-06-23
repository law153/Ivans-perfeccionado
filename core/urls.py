from django.urls import path,include
from django.conf.urls import handler404
from .views import mostrarIndex, mostrarNosotros, mostrarRegistro,mostrarIni_sesion, mostrarOlv_contra, mostrarPregunta, mostrarProducto, mostrarCategoria, mostrarIndexAdm, mostrarPerfilAdm, mostrarCategoriaAdm, mostrarAgregar, mostrarEditarPerfilAdm, mostrarCambioContraAdm, mostrarProductoAdm, mostrarEditarRol, mostrarProductoCli, mostrarCategoriaCli, mostrarMetodoPago, mostrarNosotrosCli, mostrarPerfilCli, mostrarIndexCli, mostrarCarritoCli, mostrarCambioContraCli, mostrarEditarPerfilCli,registrarUsuario,consultar, agregarProducto, inicioSesion, agregarAlCarrito, consultarCli, editarProducto, eliminarProducto, cierreSesion,mostrarError, editarPerfilCli, editarPerfilAdm, eliminarCuenta, revisarDatos, cambiarClaveAdm, cambiarClaveCli, olvideClave, editarRol, sacarDelCarro, cambiarCantidad, mostrarHistorial, mostrarCompra, mostrarConsultas, mostrarPedidos, mostrarDetallePedido, cancelarPedido, iniciar_transaccion, confirmar_transaccion, exitoCompra,errorCarrito,pagoRechazado
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
    path('cierreSesion/',cierreSesion,name="cierreSesion"),
    path('revisarDatos/',revisarDatos,name="revisarDatos"),
    path('olvideClave/',olvideClave,name="olvideClave"),
    ### Paginas cliente###
    path('producto_cli/<id_prod>',mostrarProductoCli,name="mostrarProductoCli"),
    path('principal_cli/',mostrarIndexCli,name="mostrarIndexCli"),
    path('carrito_cli/',mostrarCarritoCli,name="mostrarCarritoCli"),
    path('metodo_de_pago/<id_compra>',mostrarMetodoPago,name="mostrarMetodoPago"),
    path('nosotros_cli/',mostrarNosotrosCli,name="mostrarNosotrosCli"),
    path('editar_perfil_cli/',mostrarEditarPerfilCli,name="mostrarEditarPerfilCli"),
    path('perfil_cli/',mostrarPerfilCli,name="mostrarPerfilCli"),
    path('cambio_de_contrasena_cli/',mostrarCambioContraCli,name="mostrarCambioContraCli"),
    path('categoria_cli/<id_cate>',mostrarCategoriaCli,name="mostrarCategoriaCli"),
    path('agregarAlCarrito/',agregarAlCarrito, name="agregarAlCarrito"),
    path('mostrarHistorial/',mostrarHistorial, name="mostrarHistorial"),
    path('mostrarCompra/<idVenta>',mostrarCompra, name="mostrarCompra"),
    path('consultarCli/',consultarCli,name="consultarCli"),
    path('editarPerfilCli/',editarPerfilCli,name="editarPerfilCli"),
    path('eliminarCuenta/<id_user>',eliminarCuenta,name="eliminarCuenta"),
    path('cambiarClaveCli',cambiarClaveCli,name="cambiarClaveCli"),
    path('sacarDelCarro/<cod_detalle>',sacarDelCarro,name="sacarDelCarro"),
    path('cambiarCantidad/<cod_detalle>',cambiarCantidad,name="cambiarCantidad"),
    path('cancelarPedido/<idVenta>',cancelarPedido,name="cancelarPedido"),
    path('exitoCompra', exitoCompra, name="exitoCompra"),
    ### Paginas admin###
    path('principal_adm/',mostrarIndexAdm,name="mostrarIndexAdm"),
    path('categoria_adm/<id_cate>', mostrarCategoriaAdm, name="mostrarCategoriaAdm"),
    path('perfil_adm/',mostrarPerfilAdm, name="mostrarPerfilAdm"),
    path('agregar/', mostrarAgregar, name="mostrarAgregar"),
    path('editar_perfil_adm/', mostrarEditarPerfilAdm, name="mostrarEditarPerfilAdm"),
    path('cambio_contra_adm/', mostrarCambioContraAdm, name="mostrarCambioContraAdm"),
    path('producto_adm/<id_prod>', mostrarProductoAdm, name="mostrarProductoAdm"),
    path('consultas/', mostrarConsultas, name='mostrarConsultas'),
    path('editar_rol/', mostrarEditarRol, name="mostrarEditarRol"),
    path('listado_pedidos/',mostrarPedidos, name="mostrarPedidos"),
    path('detalle_pedido/<idPedido>',mostrarDetallePedido, name="mostrarDetallePedido"),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('editarProducto/', editarProducto, name="editarProducto"),
    path('eliminarProducto/<id_prod>', eliminarProducto, name="eliminarProducto"),
    path('editarPerfilAdm/',editarPerfilAdm,name="editarPerfilAdm"),
    path('cambiarClaveAdm/',cambiarClaveAdm,name="cambiarClaveAdm"),
    path('editarRol/<id>', editarRol, name="editarRol"),
    ### WebPay ###
    path('iniciar_transaccion/', iniciar_transaccion, name="iniciar_transaccion"),
    path('confirmar_transaccion/', confirmar_transaccion, name="confirmar_transaccion"),
    path('errorCarrito/', errorCarrito, name="errorCarrito"),
    path('pagoRechazado/', pagoRechazado, name="pagoRechazado"),
    ### Errores ###
    path('error/',mostrarError,name="mostrarError"),
   

]