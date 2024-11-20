document.addEventListener('DOMContentLoaded', function() { //Espera a que todo el contenido este cargado 
    const inputBusqueda = document.getElementById('search');// selecciona el capo de entrada que busque el usuario 

    const botonesVet = document.querySelectorAll('[data-Localidad]');//Selecciona todos los elementos (botones) que tienen el atributo personalizado "data-Localidad"
    inputBusqueda.addEventListener('input', function(){
        filtroVetLocalidad();//llama a la funcion dependiendo 

    });

    // Llama a la función para filtrar las localidades según lo que se escribe
    function filtroVetLocalidad () {
        //filtra los botones segun lo que haya escrito el usuario.
        const texto = inputBusqueda.value.toLowerCase();
        //minúsculas
        botonesVet.forEach(boton => { 
        //Recorre todos los botones 
            const localidad = boton.getAttribute("data-Localidad").toLowerCase();
             if (localidad.includes(texto)) {
         // Verifica si el texto del input está incluido en el valor de "data-Localidad"
                boton.style.display = '';
         //muestra el boton 
            } else {
                boton.style.display = 'none';
        //si no esta lo saca de cambaindo su estilo de visualización 
           }
        }); 
    }

});