from Personaje_clase import Personaje
#nombre, altura, velocidad, resistencia, fuerza

menuInicio = '''
    //////////////////////////////////////////
    /     1 - Crear Personaje                /
    /     2 - Mostrar Personaje              /
    /     3 - Salir                          /                
    ////////////////////////////////////////// ''' 

cantidadPersonaje = 0
personajes = []

while True:
    print(menuInicio)
    opcion = int(input("Seleccione una opcion:"))

    if opcion == 1:
        nombre = input("Escribe el nombre del personaje: ")
        altura = input("Escribe la altura de tu persoanje: ")
        velocidad = input("Escribe la velocidad de tu personaje: ")
        fuerza = input("Escribe la fuerza del personaje: ")
        resistencia = input("Escribe la resistecia de tu personaje: ")
        
        cantidadPersonaje = cantidadPersonaje + 1
        nuevo_personaje = Personaje(nombre, altura, velocidad, fuerza, resistencia)
        personajes.append(nuevo_personaje)

        cantidadPersonaje = 1
        print(f"El personaje {nuevo_personaje.nombre} ha sido creado ")
        print(f"Cantidad de personajes creados: {cantidadPersonaje}")
    #Crea los personajes, te muestra la cantidad de personajes que hay
    elif opcion == 2:
      if cantidadPersonaje == 0:
          print("No se encuntran personajes")
      else:
          print("Iniciado el juego con los personajes")
          for personaje in personaje:
           print(f"{personaje.nombre}")
      continue
    #Muestra si hay o no personajes gurdados.
  
    elif opcion == 3:
         print("Nos vemos luego")
    break
    #Cierra el código 
  
  