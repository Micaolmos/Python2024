document.addEventListener('DOMContentLoaded', function() { //trae el texto del usuario que agrego en el campo buscar 
    const inputBusqueda = document.getElementById('search-input');// selecciona el codigo de html y css que quiero que busque coincide

    const botonesVet = document.querySelectorAll('.vet-locations button');//guardo todo lo que este en esa clase

    inputBusqueda.addEventListener('input', function(){
        filtroVetLocalidad();//llama a la funcion 

    });


    function filtroVetLocalidad () {
        const texto = inputBusqueda. value.toLowerCase();
        botonesVet.forEach(boton => { 
            const localidad = boton.getAttribute("data-localidad").toLowerCase();
             if (localidad.includes(texto)) {
            boton.style.display = '';
            } else {
              boton.style.display = 'none';
           }
        }); 
    }

});