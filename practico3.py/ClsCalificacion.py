import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Calificacion:
    # Método constructor que inicializa las propiedades del objeto Calificación
    def __init__(self, id_estudiante, id_materia, nota,fecha):
        id_estudiante == id_estudiante #ID del estudiante
        id_materia == id_materia #ID de la materia 
        nota == nota # Nota del estudiante
        fecha == fecha # Fecha del estudiante 
    # Método para guardar la información de la calificación en la base de datos.
    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos de las calificaciones. 
        c.execute('INSERT INTO Calificación (id_estudiante, id_materia) VALUES (?,?,?)',
                (self.id_estudiante, self.id_materia, self.nota, self.fecha))
        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todas las calificaciones registradas en la base de datos.
    @staticmethod
    def obtener_calificaciones():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Calificaciones'.
        c.execute('SELECT * FROM Calificaciones')

        calificaciones = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return calificaciones# Devolver la lista de las calificaciones.          