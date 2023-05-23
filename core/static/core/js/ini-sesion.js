$(document).ready(function(){

    $("#ini-sesion").submit(function(e){

        /*Variables*/
 
        var correo = $("#correo_ini").val();
        var clave = $("#contra_ini").val();

        let msj = "";
        let enviar = false;

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
            e.preventDefault();

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
            e.preventDefault();

        }else{
            $("#alerta_contra").html("");
        }

        msj = "";

        
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
