$(document).ready(function(){

    $("#pregunta").submit(function(e){

        /*Variables*/

        var rut = $("#rut").val();
        var dvrut = $("#dvrut").val();
        var pregunta = $("#preg").val();
        var respuesta = $("#respuesta").val();

        let msj = "";
        let enviar = false;

        /*Validaciones rut*/

        if(rut.trim().length === 0 || dvrut.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } 

        if(enviar){
            $("#alerta_rut").html(msj);
            e.preventDefault();

        }else{
            $("#alerta_rut").html("");
        }

        msj = "";   

        /*Validaciones pregunta*/

        if(pregunta == 0){
            msj += "Seleccione una pregunta<br>";
            enviar = true;
        }

        if(enviar){
            $("#alerta_preg").html(msj);
            e.preventDefault();

        }else{
            $("#alerta_preg").html("");
        }
        
        msj= "";

        /*Validaciones respuesta*/ 

        if(respuesta.trim().length === 0){
            msj += "La respuesta esta vacia!<br>";
            enviar = true;
        }

        if(enviar){
            $("#alerta_resp").html(msj);
            e.preventDefault();

        }else{
            $("#alerta_resp").html("");
        }

        msj="";
        
    });

    

});
