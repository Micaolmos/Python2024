import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Estudiante:
    # Método constructor que inicializa las propiedades del objeto Estudiante.
    def __init__(self, nombre, edad, año_id):
        self.nombre = nombre # Nombre del estudiante.
        self.edad = edad # Edad del estudiante.
        self.año_id = año_id # ID del año academico del estudiante.

    # Método para guardar la información del estudiante en la base de datos.
    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos del estudiate. 
        c.execute('INSERT INTO Estudiante (nombre, edad, año_id) VALUES (?,?,?)',
                (self.nombre, self.edad, self.año_id))

        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todos los estudiantes registrados en la base de datos.
    @staticmethod
    def obtener_estudiantes():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor 