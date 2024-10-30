import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Profesor:
    # Método constructor que inicializa las propiedades del objeto Profesor.
    def __init__(self, nombre, edad):
        self.nombre = nombre # Nombre del profesor/ra.
        self.edad = edad #Edad del profesor/ra.

    # Método para guardar la información de el/la prosor/ra en la base de datos.
    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.
        # Ejecutar una consulta SQL para insertar los datos de la profesor/ra.
        c.execute('INSERT INTO Profesor/ra (nombre, edad) VALUES (?,?,?)',
                (self.nombre)
                (self.edad))
        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todos los profesores registrados en la base de datos.
    @staticmethod
    def obtener_profesor():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Profesores'.
        c.execute('SELECT * FROM Profesores')

        profesores  = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return profesores # Devolver la lista de materias          