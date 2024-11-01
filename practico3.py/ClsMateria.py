import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Materia:
    # Método constructor que inicializa las propiedades del objeto Materias
    def __init__(self, id_materia, nombre_materia, curso_materia, descripcion, horario  ):
        self.id_materia = id_materia #ID de la materia 
        self.nombre_materia = nombre_materia #Nombre de la materia 
        self.curso_materia = curso_materia #Curso donde pertenece la materia 
        self.descripcion = descripcion #Descripción de la materia.
        self.horario = horario #Horario de la materia 
    # Método para guardar la información de la materia en la base de datos.
    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos de la materia.
        c.execute('INSERT INTO Materia (nombre) VALUES (?,?,?)',
                (self.nombre))
        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todas las materias registrados en la base de datos.
    @staticmethod
    def obtener_materias():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Materias'.
        c.execute('SELECT * FROM Materias')

        materias = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return materias # Devolver la lista de materias          