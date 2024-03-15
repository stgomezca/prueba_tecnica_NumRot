import re


class Usuario:
    def __init__(self, numero_documento, primer_nombre, segundo_nombre, primer_apellido,
                 segundo_apellido, telefono, correo, direccion, edad, genero, base_datos):
        self.numero_documento = numero_documento
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.edad = edad
        self.genero = genero
        self.base_datos = base_datos

        self.campos_obligatorios = {
            "Número de documento": self.numero_documento,
            "Primer Nombre": self.primer_nombre,
            "Primer Apellido": self.primer_apellido,
            "Dirección": self.direccion,
            "Edad": self.edad,
        }

    def validar_campos(self):
        campos_vacios = []
        for key, value in self.campos_obligatorios.items():
            if value == "":
                campos_vacios.append(key)
        return campos_vacios

    def validar_datos(self):
        # Validar que el número de documento solamente contiene números
        if not self.numero_documento.isdigit():
            return "El campo Número de Documento solamente admite números"

        # Validar que el teléfono solamente contiene números si hay datos en teléfono
        elif self.telefono:
            if not self.telefono.isdigit():
                return "El campo Teléfono solamente admite números"
            else:
                return ""

        # Validar que el correo tenga patrón de correo válido cuando haya información en correo
        elif self.correo:
            if not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", self.correo):
                return "El correo no es válido"
            else:
                return ""

        # Validar que la edad solamente contiene números
        elif not self.edad.isdigit():
            return "El campo Edad solamente admite números"

        else:
            return ""

    def agregar_datos(self):
        self.base_datos.agregar_datos_usuario(self)
