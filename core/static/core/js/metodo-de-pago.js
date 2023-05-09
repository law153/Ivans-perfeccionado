$(document).ready(function(){
    $("#metodo-de-pago").submit(function(e){
        e.preventDefault();
        //VARIABLES
        var eleccion = $("#eleccion").val();
        let msj = "";
        let enviar = false;
        //VALIDACION
        if(eleccion == 0){
            msj += "Seleccione un metodo de pago<br>";
            enviar = true;
        }
        if(enviar){
            $("#alerta_metodo").html(msj);
        }else{
            $("#alerta_metodo").html("");
        }
    });
});