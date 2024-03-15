from tkinter import END
from interfaz_grafica_bd.usuario.usuario import Usuario
from interfaz_grafica_bd.bd.base_de_datos import BaseDatos
from interfaz_grafica_bd.interfaz_grafica.interfaz_grafica_secundaria import VentanaSecundaria
import customtkinter as ctk
import CTkMessagebox
from PIL import Image

# Configuraciones globales de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class InterfazGrafica(ctk.CTk):
    def __init__(self, base_datos: BaseDatos, **kwargs):
        self.base_datos = base_datos

        # Creación de la ventana principal
        super().__init__(**kwargs)
        self.title("Formulario de datos")
        self.geometry("800x600")
        self.resizable(False, False)

        # Creación del frame principal
        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack()

        # Frame de imagen
        self.imagen_frame = ctk.CTkFrame(master=self.frame)
        self.imagen_frame.grid(row=0, column=0, pady=5, padx=20)
        self.imagen = ctk.CTkImage(dark_image=Image.open("interfaz_grafica_bd/interfaz_grafica/tower-stones.jpg"),
                                   size=(360, 500))
        self.imagen_label = ctk.CTkLabel(master=self.imagen_frame, image=self.imagen, text="")
        self.imagen_label.pack()

        # Frame de información del usuario
        self.infousuario = ctk.CTkScrollableFrame(master=self.frame, width=300)
        self.infousuario.grid(row=0, column=1, pady=5, padx=10, sticky="nsew")
        self.infousuario.grid_rowconfigure(0, weight=1)
        self.infousuario.grid_columnconfigure(0, weight=1)

        # Creación de labels
        self.numero_documento = ctk.CTkLabel(master=self.infousuario, text="Número de Documento", anchor="w")
        self.primer_nombre = ctk.CTkLabel(master=self.infousuario, text="Primer Nombre", anchor="w")
        self.segundo_nombre = ctk.CTkLabel(master=self.infousuario, text="Segundo Nombre", anchor="w")
        self.primer_apellido = ctk.CTkLabel(master=self.infousuario, text="Primer Apellido", anchor="w")
        self.segundo_apellido = ctk.CTkLabel(master=self.infousuario, text="Segundo Apellido", anchor="w")
        self.telefono = ctk.CTkLabel(master=self.infousuario, text="Teléfono", anchor="w")
        self.correo = ctk.CTkLabel(master=self.infousuario, text="Correo", anchor="w")
        self.direccion = ctk.CTkLabel(master=self.infousuario, text="Dirección", anchor="w")
        self.edad = ctk.CTkLabel(master=self.infousuario, text="Edad", anchor="w")
        self.genero = ctk.CTkLabel(master=self.infousuario, text="Género", anchor="w")

        # Posicionamiento de labels
        self.numero_documento.grid(row=0, column=0, sticky="ew")
        self.primer_nombre.grid(row=2, column=0, sticky="ew")
        self.segundo_nombre.grid(row=4, column=0, sticky="ew")
        self.primer_apellido.grid(row=6, column=0, sticky="ew")
        self.segundo_apellido.grid(row=8, column=0, sticky="ew")
        self.telefono.grid(row=10, column=0, sticky="ew")
        self.correo.grid(row=12, column=0, sticky="ew")
        self.direccion.grid(row=14, column=0, sticky="ew")
        self.edad.grid(row=16, column=0, sticky="ew")
        self.genero.grid(row=18, column=0, sticky="ew")

        # Creación de entries
        self.numero_documento_entry = ctk.CTkEntry(master=self.infousuario)
        self.primer_nombre_entry = ctk.CTkEntry(master=self.infousuario)
        self.segundo_nombre_entry = ctk.CTkEntry(master=self.infousuario)
        self.primer_apellido_entry = ctk.CTkEntry(master=self.infousuario)
        self.segundo_apellido_entry = ctk.CTkEntry(master=self.infousuario)
        self.telefono_entry = ctk.CTkEntry(master=self.infousuario)
        self.correo_entry = ctk.CTkEntry(master=self.infousuario)
        self.direccion_entry = ctk.CTkEntry(master=self.infousuario)
        self.edad_entry = ctk.CTkEntry(master=self.infousuario)
        self.genero_entry = ctk.CTkComboBox(master=self.infousuario, values=["Hombre", "Mujer", "Otro"])

        # Posicionamiento de entries
        self.numero_documento_entry.grid(row=1, column=0, sticky="ew")
        self.primer_nombre_entry.grid(row=3, column=0, sticky="ew")
        self.segundo_nombre_entry.grid(row=5, column=0, sticky="ew")
        self.primer_apellido_entry.grid(row=7, column=0, sticky="ew")
        self.segundo_apellido_entry.grid(row=9, column=0, sticky="ew")
        self.telefono_entry.grid(row=11, column=0, sticky="ew")
        self.correo_entry.grid(row=13, column=0, sticky="ew")
        self.direccion_entry.grid(row=15, column=0, sticky="ew")
        self.edad_entry.grid(row=17, column=0, sticky="ew")
        self.genero_entry.grid(row=19, column=0, sticky="ew")

        # Agregar padding a los elementos del frame

        for elemento in self.infousuario.winfo_children():
            elemento.grid_configure(padx=10, pady=5)

        # Frame de botones
        self.botones = ctk.CTkFrame(master=self.frame)
        self.botones.grid(row=1, column=0, columnspan=2,pady=10, padx=10)
        self.botones.grid_rowconfigure(0, weight=1)
        self.botones.grid_columnconfigure(0, weight=1)

        # Creación de botones
        self.limpiar = ctk.CTkButton(master=self.botones, text="Limpiar campos", command=self.limpiar_campos)
        self.ingresar_informacion = ctk.CTkButton(master=self.botones, text="Ingresar información",
                                                  command=self.crear_usuario)
        self.analizar_informacion = ctk.CTkButton(master=self.botones, text="Analizar información",
                                                  command=self.nueva_ventana)

        # Posicionamiento de botones
        self.limpiar.grid(row=0, column=0)
        self.ingresar_informacion.grid(row=0, column=1)
        self.analizar_informacion.grid(row=0, column=2)

        # Agregar padding a cada elemento

        for elemento in self.botones.winfo_children():
            elemento.grid_configure(padx=20, pady=5)

        self.mainloop()

    def limpiar_campos(self):
        self.numero_documento_entry.delete(0, END)
        self.primer_nombre_entry.delete(0, END)
        self.segundo_nombre_entry.delete(0, END)
        self.primer_apellido_entry.delete(0, END)
        self.segundo_apellido_entry.delete(0, END)
        self.telefono_entry.delete(0, END)
        self.correo_entry.delete(0, END)
        self.direccion_entry.delete(0, END)
        self.edad_entry.delete(0, END)

    def crear_usuario(self):

        # Crear un usuario con los valores de los entry
        usuario = Usuario(
            self.numero_documento_entry.get().strip(),
            self.primer_nombre_entry.get().strip(),
            self.segundo_nombre_entry.get().strip(),
            self.primer_apellido_entry.get().strip(),
            self.segundo_apellido_entry.get().strip(),
            self.telefono_entry.get().strip(),
            self.correo_entry.get().strip(),
            self.direccion_entry.get().strip(),
            self.edad_entry.get().strip(),
            self.genero_entry.get(),
            base_datos=self.base_datos
        )

        # Validar que ninguno de los campos obligatorios esté en blanco
        if len(Usuario.validar_campos(usuario)) > 0:
            campos = ""
            for campo in Usuario.validar_campos(usuario):
                campos += f"\n{campo}"
            CTkMessagebox.CTkMessagebox(title="Error", message=f"Los siguientes campos son obligatorios: {campos}")
            return

        # Validar el tipo de dato
        if len(Usuario.validar_datos(usuario)) > 0:
            CTkMessagebox.CTkMessagebox(title="Error", message=Usuario.validar_datos(usuario))
            return

        # Una vez realizada la validación, se procede a guardar los datos en la base de datos
        usuario.agregar_datos()

        self.limpiar_campos()
        CTkMessagebox.CTkMessagebox(title="Éxito", message="Información guardada correctamente")

    def nueva_ventana(self):
        if self.base_datos.numero_registros() >= 10:
            self.withdraw()
            ventana_secundaria = VentanaSecundaria(self)
        else:
            CTkMessagebox.CTkMessagebox(title="Error",
                                        message=f"La base de datos debe tener al menos 10 registros, "
                                                f"actualmente tiene {self.base_datos.numero_registros()} registros")
