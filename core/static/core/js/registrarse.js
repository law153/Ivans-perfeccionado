$(document).ready(function(){

    $("#registro").submit(function(e){
        e.preventDefault();

        /*Variables*/

        var rut = $("#rut").val();
        var dvrut = $("#dvrut").val();
        var nombre = $("#nombre").val();
        var apellido = $("#apellido").val();
        var telefono = $("#fono").val(); 
        var direccion = $("#direc").val(); 
        var correo = $("#correo").val();
        var clave = $("#contra").val();
        var clave_conf = $("#contra_confirm").val();

        let msj = "";
        let enviar = false;
        var letra; /*Una variable común para guardar las primeras letras */

        /*Validaciones rut*/

        if(rut.trim().length === 0 || dvrut.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

        
        
            if(rut.trim().length != 8){
                msj += "El rut debe ser valido (8 caracteres)<br>";
                enviar = true;
            }
            
            if(dvrut.trim().length != 1){
                msj += "El digito verificador debe ser valido (1 caracter)<br>";
                enviar = true;
            }

            if(tieneLetra(rut) || tieneLetra(dvrut)){
                msj += "El rut no puede contener letras<br>";
                enviar = true;
            }

            if(tieneEsp(rut) || tieneEsp(dvrut)){
                msj += "El rut no puede contener caracteres especiales<br>";
                enviar = true;
            }

            if(!validarRun(rut,dvrut)){
                msj += "El rut no es valido";
                enviar = true;
            }

        }

        if(enviar){
            $("#alerta_rut").html(msj);

        }else{
            $("#alerta_rut").html("");
        }

        msj = "";
        /*Validaciones nombre */

        if(nombre.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(nombre.trim().length < 3 || nombre.trim().length > 30){
                msj += "El nombre debe ser entre 3 y 30 caracteres<br>";
                enviar = true;
            }

            letra = nombre.charAt(0);

            if(!esMayuscula(letra)){
                msj += "La primera letra debe ser mayúscula<br>";
                enviar = true;
            }

            if(tieneNum(nombre)){
                msj += "El nombre no debe contener un número<br>";
                enviar = true;
            }

            if(tieneEspNom(nombre) ){
                msj += "El nombre no debe contener un caracteres especiales<br>";
                enviar = true;
            }

        }
    

        if(enviar){
            $("#alerta_nombre").html(msj);

        }else{
            $("#alerta_nombre").html("");
        }


        msj = "";
        /*Validaciones apellido */

        if(apellido.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(apellido.trim().length < 4 || apellido.trim().length > 30){
                msj += "El apellido debe ser entre 4 y 30 caracteres<br>";
                enviar = true;
            }

            letra = apellido.charAt(0);

            if(!esMayuscula(letra)){
                msj += "La primera letra debe ser mayúscula<br>";
                enviar = true;
            }
            
            if(tieneNum(apellido)){
                msj += "El nombre no debe contener un número<br>";
                enviar = true;
            }

            if(tieneEspNom(apellido)){
                msj += "El nombre no debe contener un caracteres especiales<br>";
                enviar = true;
            }
        }

        if(enviar){
            $("#alerta_apellido").html(msj);

        }else{
            $("#alerta_apellido").html("");
        }

        msj = "";
        /*Validaciones telefono*/

        if(telefono.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(telefono.trim().length != 8){
                msj += "El telefono debe ser valido (8 caracteres)<br>";
                enviar = true;
            }

            if(tieneLetra(telefono)){
                msj += "El telefono no puede contener letras<br>";
                enviar = true;
            }

            if(tieneEsp(telefono)){
                msj += "El telefono no puede contener caracteres especiales<br>";
                enviar = true;
            }
        }
        if(enviar){
            $("#alerta_telefono").html(msj);

        }else{
            $("#alerta_telefono").html("");
        }


        msj = "";
        /*Validaciones direccion*/

        if(direccion.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(direccion.trim().length < 5 || direccion.trim().length > 100){
                msj += "La dirección debe tener una longitud entre 5 y 100 caracteres<br>";
                enviar = true;
            }

            letra = direccion.charAt(0);

            if(!esMayuscula(letra)){
                msj += "La primera letra debe ser mayúscula<br>";
                enviar = true;
            }

            if(!tieneLetra(direccion)){
                msj += "La dirección debe contener al menos una letra<br>";
                enviar = true;
            }

            if(!tieneNum(direccion)){
                msj += "La dirección debe contener al menos un número<br>";
                enviar = true;
            }

            if(tieneEspNom(direccion)){
                msj += "El nombre no debe contener un caracteres especiales<br>";
                enviar = true;
            }
        }

        if(enviar){
            $("#alerta_direccion").html(msj);

        }else{
            $("#alerta_direccion").html("");
        }

        msj = "";
        /*Validaciones correo*/

        if(correo.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            var indice = correo.indexOf("@");

            var cuerpo = correo.substring(0, indice);

            var dominio = correo.substring(indice + 1);

            if(!(dominio.indexOf(".") !== -1) || (cuerpo.length <= 1 && cuerpo.length <= 64) || dominio.length < 4){ //Valida la presencia de un . en el dominio y la longitud de la parte local y el dominio.
                msj += "El correo no es valido<br>";
                enviar = true;
            }
        }

        if(enviar){
            $("#alerta_correo").html(msj);

        }else{
            $("#alerta_correo").html("");
        }

        msj = "";
        /*Validaciones clave*/

        if(clave.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{


            if(clave.trim().length < 5 || clave.trim().length > 20){
                msj += "La clave debe ser entre 5 y 20 caracteres<br>";
                enviar = true;
            }

            if(!tieneMayus(clave)){
                msj += "La clave debe contener al menos una mayuscula<br>";
                enviar = true;
            }

            if(!tieneMinus(clave)){
                msj += "La clave debe contener al menos una minuscula<br>";
                enviar = true;
            }

            if(!tieneNum(clave)){
                msj += "La clave debe contener al menos un número<br>";
                enviar = true;
            }

            if(!tieneEsp(clave)){
                msj += "La clave debe contener al menos un caracter especial<br>";
                enviar = true;
            }

        }
        
        if(enviar){
            $("#alerta_contra").html(msj);

        }else{
            $("#alerta_contra").html("");
        }

        

        msj = "";

        /**Validaciones confirmar contraseña*/
        if(clave_conf.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(clave_conf != clave){
                msj += "Las claves son distintas";
                enviar = true;
            }

        }

        if(enviar){
            $("#alerta-conf").html(msj);

        }else{
            $("#alerta-conf").html("");
        }

        msj = "";
        
    });

    function esMayuscula(letra){
        
        if(letra == letra.toUpperCase()){
            return true;
        }
        else{
            return false;
        }
         
    }

    function tieneMayus(palabra){
        if(palabra.match(/[A-Z]/)) {
            return true;
        } else{
            return false;
        }
    }

    function tieneMinus(palabra){
        if(palabra.match(/[a-z]/)) {
            return true;
        } else{
            return false;
        }
    }

    function tieneNum(palabra){
        if(palabra.match(/[0-9]/)) {
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

    function tieneEsp(palabra){
        if(palabra.match(/\W/)) {
            return true;
        } else{
            return false;
        }
    }

    function tieneEspNom(palabra) {
        if (palabra.match(/[^\w\s-'áéíóúüñ]/)) {
          return true;
        } else {
          return false;
        }
    }

    function validarRun(run, dv) {
        
        // Validar que el run tenga al menos 1 dígito y que el DV sea un dígito
        if (run.length < 1 || dv.length != 1) {
          return false;
        }
      
        // Calcular DV esperado
        var suma = 0;
        var factor = 2;
        for (var i = run.length - 1; i >= 0; i--) {
          suma += parseInt(run.charAt(i)) * factor;
          factor = factor === 7 ? 2 : factor + 1;
        }

        var dvEsperado = 11 - (suma % 11);
        // Esta parte podría necesitar revisión
        if (dvEsperado === 11) {
          dvEsperado = 0;
        } else if (dvEsperado === 10) {
          dvEsperado = 0;
        }
      
        // Validar que el DV sea igual al esperado
        return dvEsperado == dv;
    }

    

});
