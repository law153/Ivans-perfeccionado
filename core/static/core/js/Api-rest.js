$(document).ready(function(){
    var a = 1;
    
    $("#boton").click(function(){

        if(a === 1){

            $.ajax({
                url: 'https://randomuser.me/api/',
                dataType: 'json',
                success: function(data) {
                  console.log(data);
                  a = 2;
                  $.each(data.results, function(i, item){
                    $("#tabla").append("<tr>"+
                                            "<td> <img class='cli-foto' src='"+item.picture.large+"' alt='No hay imagen'></td>"+
                                            "<td class='nombre-cli'>"+item.name.first+" "+item.name.last+"</td>");
                  });
                }
                
            });
    
        }

        
        

    });

});