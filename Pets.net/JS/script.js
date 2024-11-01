document.addEventListener('DOMContentLoaded', function() { //trae el texto del usuario que agrego en el campo buscar 
    const inputBusqueda = document.getElementById('search');// selecciona el codigo de html y css que quiero que busque coincide

    const botonesVet = document.querySelectorAll('[data-Localidad]');//guardo todo lo que este en esa clase

    inputBusqueda.addEventListener('input', function(){
        filtroVetLocalidad();//llama a la funcion 

    });


    function filtroVetLocalidad () {
        const texto = inputBusqueda.value.toLowerCase();
        botonesVet.forEach(boton => { 
            const localidad = boton.getAttribute("data-Localidad").toLowerCase();
             if (localidad.includes(texto)) {
                boton.style.display = '';
            } else {
                boton.style.display = 'none';
           }
        }); 
    }

});