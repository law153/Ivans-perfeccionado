$(document).ready(function(){
    $("#contacto-cli").submit(function(e){

        /*Variables*/
        var nombre = $("#nom").val();
        var asunto = $("#asunto").val();
        var cuerpo = $("#mensaje").val();
        let msj = "";
        let enviar = false;
        var letra; /*Una variable común para guardar las primeras letras */
       /*Validaciones nombre */
       if(nombre.trim().length === 0 || asunto.trim().length === 0 || cuerpo.trim().length === 0){            
            msj += "Debe llenar todos los campos";
            enviar = true;
        } else{
            if(nombre.trim().length < 3 || nombre.trim().length > 20){
                msj += "El nombre debe ser entre 3 y 20 caracteres<br>";
                enviar = true;
            }
            letra = nombre.charAt(0);
            if(!esMayuscula(letra)){
                msj += "La primera letra debe ser mayúscula<br>";
                enviar = true;
            }
            if(tieneEspNom(nombre)){
                msj += "El nombre no puede contener caracteres especiales<br>";
                enviar = true;
            }
            if(tieneNum(nombre)){
                msj += "El nombre no puede contener números<br>";
                enviar = true;
            }
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
