def menu():
    menuInicio = '''
    //////////////////////////////////////////
    /     1 - Añadir una tarea               /
    /     2 - Ver todas las tareas           /
    /     3 -Marcar una tarea como completa  /
    /     4 - Salir                          /
    ////////////////////////////////////////// ''' 
    print(menuInicio)
opcion = int(input("Ingrese la opcion seleccionada: "))
opcion = menu()

listaTareas=[]
diccionario = {}
while True: 
    menu()
    opcion = int(input("ingrese una opcion:"))
    if opcion == 1:
        Tarea:int(input("Ingresa la nueva tarea:"))
        print("Se guardo tu nueva tarea")
        listaTareas.append

    elif opcion == 2: 
        if not listaTareas:
         print("No hay tareas en la lista.")
    else:
         print(listaTareas =[])

    elif opcion == "3":
            completar_tarea(tareas)
    
    elif opcion == "4":
            print("¡Nos vemos luego, chau!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
            continue
    
    