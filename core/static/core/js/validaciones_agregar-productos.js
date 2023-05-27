$(document).ready(function(){
    $("#form_agregar").submit(function(e){

        //--Variables--

        //--Permite que solo se suban ciertos formatos de archivos
        const imagen = $("#imagen").prop('files')[0];
        const extensionesPermitidas = ['jpg', 'png'];
        //--

        var nombre = $("#nombre").val();
        var descripcion = $("#descripcion").val();
        var precio = $("#precio").val();
        var stock = $("#stock").val();

        let msj = "";
        let enviar = "false";

        //--Validacion Imágenes

        if ($("#imagen").val() === "") {
            msj += "Debe seleccionar una imagen<br>";
            enviar = "true";
        } else {

            if(!validarExtension(imagen, extensionesPermitidas)){
                msj += "El archivo seleccionado no tiene una extensión permitida<br>";
                $('#imagen').val('');
                enviar = "true";
            }
        }

        if(enviar){
            $("#alerta_imagen-prod").html(msj);
            e.preventDefault();

        }else{
            $("#alerta_imagen-prod").html("");
        }

        msj="";

        //Fin validacion imágen

        //--Validaciones Nombre

        if(nombre.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(nombre.trim().length < 3 || nombre.trim().length > 100){
            msj += "El nombre del producto debe poseer entre 3 y 100 caracteres<br>";
            enviar = "true";
            }

            if(tieneEspNom(nombre) ){
                msj += "El nombre no debe contener caracteres especiales<br>";
                enviar = "true";
            }

        }

        if(enviar){
            $("#alerta_nombre-prod").html(msj);
            e.preventDefault();

        }else{
            $("#alerta_nombre-prod").html("");
        }

        msj="";

        //Fin validaciones Nombre--

        //--Validaciones Descripcion

        if(descripcion.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(descripcion.length < 3  || descripcion.length > 300){
                msj += "La descripcion debe contener entre 3 y 300 caracteres<br>";
                enviar = "true";
            }

            if(tieneEspNom(descripcion) ){
                msj += "La descripción no debe contener caracteres especiales<br>";
                enviar = "true";
            }
        }

        if(enviar){
            $("#alerta_descripcion-prod").html(msj);
            e.preventDefault();
        }else{
            $("#alerta_descripcion-prod").html("");
        }

        msj="";

        //Fin validaciones Descripcion--

        //--Validaciones Precio

        if(precio.trim().length === 0){
            
            msj += "Debe llenar estos campos";
            enviar = true;

        } else{

            if(precio <= 0){
                msj += "El precio debe tener un valor mayor a 0<br>";
                enviar = "true";
            }

            if(tieneEsp(precio)){
                msj += "El precio no debe contener caracteres especiales<br>"
                enviar = "true";
            }

            if(tieneLetra(precio)){
                msj += "El precio no debe contener ninguna letra<br>";
                enviar = "true";
            }
        }

        if(enviar){
            $("#alerta_precio-prod").html(msj);
            e.preventDefault();
        }else{
            $("#alerta_precio-prod").html("");
        }

        msj="";

        //Fin validaciones Precio--

        //--Validaciones Stock

        if(stock.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(stock < 0 ){
                msj += "El stock no puede ser menor a 0<br>";
                enviar = "true";
            }

            if(tieneEsp(stock)){
                msj += "El stock no puede contener caracteres especiales<br>";
                enviar = "true";
            }
        }

        if(enviar){
            $("#alerta_stock-prod").html(msj);
            e.preventDefault();
        }else{
            $("#alerta_stock-prod").html("");
        }

        msj="";

        //Fin validaciones Stock--

    });

    //Funciones

    function tieneEspNom(palabra) {
        if (palabra.match(/[^\w\s-'áéíóúüñ/]/)) {
          return true;
        } else {
          return false;
        }
    }

    function validarExtension(archivo, extensionesPermitidas){
        const allowedExtensions = new RegExp(extensionesPermitidas.join('|'), 'i');

        if (!allowedExtensions.exec(archivo.name)) {
            return false;
        }

        return true;
    }

    function tieneEsp(palabra){
        if(palabra.match(/\W/)) {
            return true;
        } else{
            return false;
        }
    }

    function tieneLetra(palabra){
        if(palabra.match(/[a-zA-Z]/)) {
            return true;
        } else{
            return false;
        }
    }
});