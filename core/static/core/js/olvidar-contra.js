$(document).ready(function(){

    $("#cambio-contra").submit(function(e){

        /*Variables*/
        var clave = $("#contra_nueva").val();
        var conf_clave = $("#contra_confirm").val();

        let msj = "";
        let enviar = false;

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
            $("#alerta-nueva").html(msj);
            e.preventDefault();

        }else{
            $("#alerta-nueva").html("");
        }

        msj= "";

        /*Validar confirmar*/

        if(conf_clave.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(conf_clave != clave){
                msj += "Las contraseñas no son iguales<br>";
                enviar = true;
            }
        }
        
        if(enviar){
            $("#alerta-conf").html(msj);
            e.preventDefault();

        }else{
            $("#alerta-conf").html("");
        }

        msj= "";

        
    });

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

    function tieneEsp(palabra){
        if(palabra.match(/\W/)) {
            return true;
        } else{
            return false;
        }
    }

    

});
