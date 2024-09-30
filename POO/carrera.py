from Personaje_clase import Personaje
#nombre, altura, velocidad, resistencia, fuerza

menuInicio = '''
    //////////////////////////////////////////
    /     1 - Crear Personaje                /
    /     2 - Jugar                          /
    /     3 - Salir                          /                
    ////////////////////////////////////////// ''' 

cantidadPersonaje = 0
personajes = []

while True:
    print(menuInicio)
    opcion = int(input("Seleccione una opcion:"))

    if opcion == 1:
        nombre = input("Escribe el nombre del personaje: ")
        altura = int(input("Escribe la altura de tu persoanje: "))
        velocidad = int(input("Escribe la velocidad de tu personaje: "))
        resistencia = int(input("Escribe la resistecia de tu personaje: "))
        fuerza = int(input("Escribbe la fuerza de tu personaje: "))
  
        nuevo_personaje = Personaje(nombre, altura, velocidad, resistencia, fuerza)
        personajes.append (nuevo_personaje)

        cantidadPersonaje = 1
        print(f"El personaje {nuevo_personaje.nombre} ha sido creado ")
        print(f"Cantidad de personajes creados: {cantidadPersonaje}")
        #Crea los personajes, te muestra la cantidad de personajes que hay

    elif opcion == 2:
      if cantidadPersonaje == 0 or cantidadPersonaje == 1:
          print("Nesecitas dos personajes para jugar")
          continue
      else:
          print("Iniciado el juego con los personajes")
          for personaje in personajes:
           print(f"{personaje.nombre}")
    
    #Muestra si hay o no personajes gurdados.
  
    elif opcion == 3:
        print("Nos vemos luego")
    break
    #Cierra el código 
  
  