import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Estudiante:
    # Método constructor que inicializa las propiedades del objeto Estudiante.
    def __init__(self, nombre, edad,legajo_id, dni, apellido, fecha_nacimiento, curso, estado, email ):
        self.legajo_id = legajo_id #ID del estudiante 
        self.dni = dni #DNI del estudiante 
        self.nombre = nombre # Nombre del estudiante.
        self.apellido = apellido #Apellido del estudiante 
        self.edad = edad # Edad del estudiante.
        self.fecha_nacimiento = fecha_nacimiento #Fecha de nacimiento del estudiante
        self.curso = curso #Curso del estudiante
        self.estado = estado #Estado del estudiante
        self.email = email #Email del estudiante
    # Método para guardar la información del estudiante en la base de datos.
    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos del estudiate. 
        c.execute('INSERT INTO Estudiante (nombre, edad, año_id) VALUES (?,?,?)',
                (self.legajo_id, self.dni, self.nombre, self.apellido, self.edad, self.fecha_nacimiento, self.curso, self.estado, self.email))

        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todos los estudiantes registrados en la base de datos.
    @staticmethod
    def obtener_estudiantes():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Estudiantes'.
        c.execute('SELECT * FROM Estudiantes')

        estudiantes = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return estudiantes # Devolver la lista de estudiantes.          