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

        } 
        
        if(enviar){
            $("#alerta_contra").html(msj);
            e.preventDefault();

        }else{
            $("#alerta_contra").html("");
        }

        msj = "";

        
    });

});
