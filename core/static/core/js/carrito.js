$(document).ready(function(){
    $("#boton-cant").submit(function(e){

        /*Variables*/
        var cantidad = $("#cantidad").val();
        let msj = "";
        let enviar = false;

        if(cantidad.trim().length === 0){

            msj += "No puede dejar la cantidad vacia!";
            enviar = true;

        }

        if(enviar){
            $("#alerta-cant").html(msj);
            e.preventDefault();
        }else{
            $("#alerta-cant").html("");
        }

        msj = "";
    });

});
