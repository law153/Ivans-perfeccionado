$(document).ready(function(){
    $("#cambiar-contra-cli").submit(function(e){
        e.preventDefault();
        //--Variables--

        var contra_actual = $("#contra_actual").val();
        var contra_nueva = $("#contra_nueva").val();
        var contra_confirm = $("#contra_confirm").val();

        let msj = "";
        let enviar = "false"; //Si enviar es true, quiere decir que algo es invalido

        //--Validación Contraseña Actual

        if(contra_actual.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(contra_actual.trim().length < 5 || contra_actual.trim().length > 20){
                msj += "La clave debe ser entre 5 y 20 caracteres<br>";
                enviar = "true";
            }

            if(!tieneMayus(contra_actual)){
                msj += "La clave debe contener al menos una mayuscula<br>";
                enviar = "true";
            }

            if(!tieneMinus(contra_actual)){
                msj += "La clave debe contener al menos una minuscula<br>";
                enviar = "true";
            }

            if(!tieneNum(contra_actual)){
                msj += "La clave debe contener al menos un número<br>";
                enviar = "true";
            }

            if(!tieneEsp(contra_actual)){
                msj += "La clave debe contener al menos un caracter especial<br>";
                enviar = "true";
            }
        }

        if(enviar){
            $("#alerta-actual").html(msj);

        }else{
            $("#alerta-actual").html("");
        }

        msj = ""; 

        //Fin validaciones Contraseña Actual--

        //--Validaciones Contraseña Nueva

        if(contra_nueva.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(contra_nueva.trim().length < 5 || contra_nueva.trim().length > 20){
                msj += "La clave debe ser entre 5 y 20 caracteres<br>";
                enviar = "true";
            }

            if(!tieneMayus(contra_nueva)){
                msj += "La clave debe contener al menos una mayuscula<br>";
                enviar = "true";
            }

            if(!tieneMinus(contra_nueva)){
                msj += "La clave debe contener al menos una minuscula<br>";
                enviar = "true";
            }

            if(!tieneNum(contra_nueva)){
                msj += "La clave debe contener al menos un número<br>";
                enviar = "true";
            }

            if(!tieneEsp(contra_nueva)){
                msj += "La clave debe contener al menos un caracter especial<br>";
                enviar = "true";
            }

            if(compararContraIguales(contra_nueva, contra_actual)){
                msj += "La contraseña es igual a la actual, favor digitar una distinta<br>";
                enviar = "true";
            }
        }

        if(enviar){
            $("#alerta-nueva").html(msj);

        }else{
            $("#alerta-nueva").html("");
        }

        msj = ""; 

        //Fin Validaciones Contraseña Nueva--

        //--Validaciones Confirmar Contraseña

        if(contra_confirm.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{

            if(contra_confirm.trim().length < 5 || contra_confirm.trim().length > 20){
                msj += "La clave debe ser entre 5 y 20 caracteres<br>";
                enviar = "true";
            }

            if(!tieneMayus(contra_confirm)){
                msj += "La clave debe contener al menos una mayuscula<br>";
                enviar = "true";
            }

            if(!tieneMinus(contra_confirm)){
                msj += "La clave debe contener al menos una minuscula<br>";
                enviar = "true";
            }

            if(!tieneNum(contra_confirm)){
                msj += "La clave debe contener al menos un número<br>";
                enviar = "true";
            }

            if(!tieneEsp(contra_confirm)){
                msj += "La clave debe contener al menos un caracter especial<br>";
                enviar = "true";
            }

            if(compararContraDistintas(contra_confirm, contra_nueva)){
                msj += "La contraseña es distinta a la que ingreso, favor digitar la misma<br>";
                enviar = "true";
            }
        }

        if(enviar){
            $("#alerta-conf").html(msj);

        }else{
            $("#alerta-conf").html("");
        }

        //Fin Validaciones Confirmar Contraseña--
    
    });
    //Funciones

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

    function compararContraIguales(palabra, palabra2){
        if(palabra === palabra2){
            return true;
        }else{
            return false;
        }

    }

    function compararContraDistintas(palabra, palabra2){
        if(palabra != palabra2){
            return true;
        }else{
            return false;
        }

    }
});