$(document).ready(function(){
    $("#contacto-cli").submit(function(e){

        /*Variables*/
        var asunto = $("#asunto").val();
        var cuerpo = $("#mensaje").val();
        let msj = "";
        let enviar = false;
       if(asunto.trim().length === 0 || cuerpo.trim().length === 0){            
            msj += "Debe llenar todos los campos";
            enviar = true;
        } else{

            /*Validaciones asunto*/
            if(asunto.trim().length < 3 || asunto.trim().length > 30){
                msj += "El asunto debe ser entre 3 y 30 caracteres<br>";
                enviar = true;
            }
            /*Validaciones mensaje*/
            if(cuerpo.trim().length < 10 || cuerpo.trim().length > 200){
                msj += "El mensaje debe ser entre 10 y 200 caracteres<br>";
                enviar = true;
            }
        }
        if(enviar){
            $("#alerta").html(msj);
            e.preventDefault();

        }else{
            $("#alerta").html("");
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
    function tieneNum(palabra){
        if(palabra.match(/[0-9]/)) {
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
});
