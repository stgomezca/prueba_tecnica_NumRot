import sqlite3
from tkinter import filedialog


class BaseDatos:
    def __init__(self):
        self.ruta_archivo = ""
        self.crear_base_de_datos()

    def crear_base_de_datos(self):
        self.ruta_archivo = filedialog.asksaveasfilename(defaultextension=".db",
                                                         filetypes=[("Archivos de base de datos SQLite", "*.db")])

        # Si se especificó la ruta, crear la tabla
        if self.ruta_archivo:
            connection = sqlite3.connect(self.ruta_archivo)
            query_tabla = '''CREATE TABLE IF NOT EXISTS Datos_Usuarios 
            (documento INT, primer_nombre TEXT, segundo_nombre TEXT, primer_apellido TEXT, segundo_apellido TEXT,
            telefono INT, correo TEXT, direccion TEXT, edad INT, genero TEXT)
            '''
            connection.execute(query_tabla)
            connection.close()

    # Método que ingresa en la tabla los datos del usuario
    def agregar_datos_usuario(self, usuario):
        connection = sqlite3.connect(self.ruta_archivo)

        query_agregar_datos = '''INSERT INTO Datos_Usuarios (documento, primer_nombre, segundo_nombre, 
                            primer_apellido, segundo_apellido, telefono, correo, direccion, edad, 
                            genero) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        tupla_agregar_datos = (usuario.numero_documento, usuario.primer_nombre, usuario.segundo_nombre,
                               usuario.primer_apellido, usuario.segundo_apellido, usuario.telefono,
                               usuario.correo, usuario.direccion, usuario.edad, usuario.genero)

        cursor = connection.cursor()
        cursor.execute(query_agregar_datos, tupla_agregar_datos)
        connection.commit()
        connection.close()

    # Método que cuenta cuántos registros hay hasta el momento en la base de datos
    def numero_registros(self):
        connection = sqlite3.connect(self.ruta_archivo)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Datos_Usuarios''')
        numero_registros_actuales = len(cursor.fetchall())
        connection.close()
        return numero_registros_actuales

    # Método para obtener los nombres completos de los usuarios registrados
    def nombres_completos(self):
        connection = sqlite3.connect(self.ruta_archivo)
        cursor = connection.cursor()
        cursor.execute('''SELECT primer_nombre, segundo_nombre, primer_apellido, segundo_apellido 
                        FROM Datos_Usuarios''')
        registros = cursor.fetchall()
        nombres_completos = []
        # Extraer los nombres de tupla a lista
        for registro in registros:
            # En caso de que el usuario no haya ingresado alguno de los campos
            nombre = (f"{registro[0]} {registro[1]} {registro[2]} {registro[3]}").split()
            nombre_completo = " ".join(nombre)
            nombres_completos.append(nombre_completo)
        connection.close()
        return nombres_completos

    # Método para contar cuántos registros tienen el género mujer
    def conteo_mujeres(self):
        connection = sqlite3.connect(self.ruta_archivo)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Datos_Usuarios WHERE genero = ?''', ("Mujer",))
        cantidad_mujeres = len(cursor.fetchall())
        connection.close()
        return cantidad_mujeres

    # Método para contar cuántos registros tienen el género hombre
    def conteo_hombres(self):
        connection = sqlite3.connect(self.ruta_archivo)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Datos_Usuarios WHERE genero = ?''', ("Hombre",))
        cantidad_hombres = len(cursor.fetchall())
        connection.close()
        return cantidad_hombres

    # Método para obtener el nombre de la persona con mayor edad en la base de datos
    def persona_mayor(self):
        connection = sqlite3.connect(self.ruta_archivo)
        cursor = connection.cursor()
        cursor.execute('''SELECT primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, MAX(edad)
                        FROM Datos_Usuarios''')
        persona_mayor = cursor.fetchone()
        nombre_persona_mayor = (f"{persona_mayor[0]} {persona_mayor[1]} {persona_mayor[2]} {persona_mayor[3]}").split()
        nombre_completo_persona_mayor = " ".join(nombre_persona_mayor)
        connection.close()
        return nombre_completo_persona_mayor

    # Método para obtener la media de edad de la base de datos
    def media_edad(self):
        connection = sqlite3.connect(self.ruta_archivo)
        cursor = connection.cursor()
        cursor.execute('''SELECT AVG(edad) FROM Datos_Usuarios''')
        media_edad = cursor.fetchone()[0]
        connection.close()
        return round(media_edad, 2)
