import customtkinter as ctk

# Configuraciones globales de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class VentanaSecundaria(ctk.CTk):
    def __init__(self, interfaz_principal , **kwargs):
        super().__init__(**kwargs)
        self.interfaz_principal = interfaz_principal
        self.title("Análisis de datos")
        self.geometry("600x350")
        self.resizable(False, False)

        # Frame principal
        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(fill="both", expand=True)

        # Frame de botones
        self.botones_frame = ctk.CTkFrame(master=self.frame)
        self.botones_frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)

        # Botones

        self.boton_nombres = ctk.CTkButton(master=self.botones_frame, text="Obtener todos los \nnombres completos",
                                           command=self.nombres)
        self.boton_conteo_hombres = ctk.CTkButton(master=self.botones_frame, text="Conteo de hombres",
                                                  command=self.hombres)
        self.boton_conteo_mujeres = ctk.CTkButton(master=self.botones_frame, text="Conteo de mujeres",
                                                  command=self.mujeres)
        self.boton_persona_mayor = ctk.CTkButton(master=self.botones_frame,
                                                 text="Obtener nombre completo \nde la persona mayor",
                                                 command=self.persona_mayor)
        self.boton_media_edad = ctk.CTkButton(master=self.botones_frame, text="Obtener media de edad",
                                              command=self.media_edad)

        # Posicionamiento botones

        self.boton_nombres.pack()
        self.boton_conteo_hombres.pack()
        self.boton_conteo_mujeres.pack()
        self.boton_persona_mayor.pack()
        self.boton_media_edad.pack()

        for elemento in self.botones_frame.winfo_children():
            elemento.pack(pady=10,  padx=10, fill="x", expand=True)

        # Frame de respuestas

        self.segundo_frame = ctk.CTkScrollableFrame(master=self.frame, width=350)
        self.segundo_frame.grid(row=0, column=1, sticky="news", padx=10, pady=10)

        self.boton_volver = ctk.CTkButton(master=self, text="Volver", command=self.volver)
        self.boton_volver.pack(fill="x", expand=True, padx=10, pady=5)


        self.mainloop()

    def limpiar_board(self):
        for elemento in self.segundo_frame.winfo_children():
            elemento.destroy()

    def nombres(self):
        self.limpiar_board()
        title_label = ctk.CTkLabel(master=self.segundo_frame, text="Los nombres completos registrados son:")
        title_label.pack()
        nombres = self.interfaz_principal.base_datos.nombres_completos()
        for nombre in nombres:
            nombre_label = ctk.CTkLabel(master=self.segundo_frame, text=nombre)
            nombre_label.pack()


    def hombres(self):
        self.limpiar_board()
        title_label = ctk.CTkLabel(master=self.segundo_frame, text="La cantidad de hombres registrados es:")
        title_label.pack()
        conteo_label = ctk.CTkLabel(master=self.segundo_frame, text=self.interfaz_principal.base_datos.conteo_hombres())
        conteo_label.pack()

    def mujeres(self):
        self.limpiar_board()
        title_label = ctk.CTkLabel(master=self.segundo_frame, text="La cantidad de mujeres registradas es:")
        title_label.pack()
        conteo_label = ctk.CTkLabel(master=self.segundo_frame, text=self.interfaz_principal.base_datos.conteo_mujeres())
        conteo_label.pack()

    def persona_mayor(self):
        self.limpiar_board()
        title_label = ctk.CTkLabel(master=self.segundo_frame, text="La persona con mayor edad registrada es:")
        title_label.pack()
        nombre_label = ctk.CTkLabel(master=self.segundo_frame, text=self.interfaz_principal.base_datos.persona_mayor())
        nombre_label.pack()

    def media_edad(self):
        self.limpiar_board()
        title_label = ctk.CTkLabel(master=self.segundo_frame, text="La media de edad del registro es:")
        title_label.pack()
        media_label = ctk.CTkLabel(master=self.segundo_frame, text=self.interfaz_principal.base_datos.media_edad())
        media_label.pack()

    def volver(self):
        self.interfaz_principal.deiconify()
        self.destroy()