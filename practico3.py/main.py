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
            Estudiante
