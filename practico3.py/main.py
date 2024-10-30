import sqlite3
import ClsEstudiante 
import ClsProfesor 
import ClsMateria 
import ClsCalificacion

#Función para conectar a la base de datos SQLite. 
def conectar__db():
    # Crear conexión a la base de datos llamada "escuelas.db".
    conn = sqlite3.connect("escuelas.db")
    return conn 

#Función principal que ejecuta el programa.
def main():
    #Establece la conexión con la base de datos.
    conn = conectar__db()
    #Crear un curso para ejecutar consultas SQL.
    cursor = conn.cursor()

    #Bucle infinito hasta que el usuario decida salir
    while True:
        print("/nSistema de Gestión Escolar")
        print("1. Agregar estudiante")
        print("2. Agregar profesor")
        print("3. Agregar materia")
        print("4. Agregar calificación")
        print("5. Mostrar estudiantes")
        print("6. Mostrar profesores")
        print("7. Mostrar materias")
        print("8. Mostrar calificaiones")
        print("9. Salir del programa")
        opcion = input("Selecione una opcion: ")

        #Procesa la opcion ingresada por el usuario.
        if opcion == "1" :
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            ClsEstudiante.agreagar(conn, nombre, edad)
        elif opcion == "2" :
            nombre = input("Nombre del profesor: ")
            edad = input("Edad del profesor: ")
            ClsProfesor.agregar(conn, nombre, edad)
        elif opcion == "3":
            nombre = input("Introduce el nombre de la materia: ")
            ClsMateria.agregar(conn, nombre)
        elif opcion == "4":
            id_estudiante = input("ID del estudiante: ")
            id_materia = input("ID de la materia: ")
            nota = input("calidficación: ")
            ClsCalificacion.agregar(conn, id_estudiante, id_materia, nota)
        elif opcion == "5":
            ClsEstudiante.mostrar_todos(conn)
        elif opcion == "6":
            ClsProfesor.mostrar_todos(conn)
        elif opcion == "7":
            ClsMateria.mostrar_todos(conn)
        elif opcion == "8":
            ClsCalificacion.mostrar_todos(conn)
        elif opcion == "9":
            print("saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

        #Cierre la coneción a la base de datos al salir del programa 
        conn.close()

    #Punto de entrada del programa
   
