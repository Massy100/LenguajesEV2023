import tkinter as tk


class PantallaCA(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.geometry("640x480")
        self.title("Carga de Archivos")

        tk.Button(self, text="Cargar AFD", width=100, height=5).pack(
            expand=True
        )
        tk.Button(self, text="Cargar AFN", width=100, height=5).pack(
            expand=True
        )
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        PantallaCA.destroy(self)