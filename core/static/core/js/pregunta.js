$(document).ready(function(){

    $("#pregunta").submit(function(e){
        e.preventDefault();

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
                msj += "El rut no es valido<br>";
                enviar = true;
            }
        }

        if(enviar){
            $("#alerta_rut").html(msj);

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

        }else{
            $("#alerta_resp").html("");
        }

        msj="";
        
    });

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
