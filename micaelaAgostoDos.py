# Función para mostrar el menú
def menu():
    menuInicio = '''
    //////////////////////////////////////////
    /     1 - Añadir una tarea               /
    /     2 - Ver todas las tareas           /
    /     3 - Marcar una tarea como completa /
    /     4 - Salir                          /
    //////////////////////////////////////////
'''
    print(menuInicio)

# Lista para almacenar las tareas
listaTareas = []

# Bucle principal
while True:
    menu()
    opcion = input("Ingrese la opción seleccionada: ")

    if opcion == "1":
        # Añadir una tarea
        tarea = input("Ingresa la nueva tarea: ")
        listaTareas.append(tarea)
        print("Se guardó tu nueva tarea.")

    elif opcion == "2":
        # Ver todas las tareas
        if not listaTareas:
            print("No hay tareas en la lista.")
        else:
            print(" Lista de tareas ")
            contador = 1
            for tarea in listaTareas:
                print(f"{contador}. {tarea}")
                contador += 1

    elif opcion == "3":
        # Marcar una tarea como completada
        if not listaTareas:
            print("No hay tareas para completar.")
        else:
            print("Lista de tareas ")
            contador = 1
            for tarea in listaTareas:
                print(f"{contador}. {tarea}")
                contador += 1

            tarea_completada = input("Selecciona el número de la tarea que completaste: ")

            try:
                # Intentamos convertir la entrada a un número
                tarea_completada = int(tarea_completada)

                # Verificamos si el número está en el rango válido
                if tarea_completada >= 1 and tarea_completada <= contador - 1:  # Usar contador - 1 ya que contador se incrementa después de la última tarea
                    listaTareas.pop(tarea_completada - 1)
                    print("Tarea completada.")
                else:
                    print("Número de tarea no válido.")
            except ValueError:
                # Si la conversión falla, significa que el usuario no ingresó un número
                print("Por favor, ingresa un número válido.")

    elif opcion == "4":
        # Salir del programa
        print("¡Nos vemos luego, chau!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
