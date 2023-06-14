import tkinter as tk
from vistas.vistaAyudaOE import PantallaAyudaOE

class PantallaOE(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.geometry("640x480")
        self.title("Optimizacion de Estados")

        tk.Button(self, text="Seleccionar AFD", width=100, height=5).pack(
            expand=True
        )
        tk.Button(self, text="Generar Reportes", width=100, height=5).pack(
            expand=True
        )
        tk.Button(self, text="Ayuda", width=100, height=5, command=self.abrir_ventanaAyudaOE).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def abrir_ventanaAyudaOE(self):
        ventanaAyudaOE = PantallaAyudaOE(self)
        ventanaAyudaOE.grab_set()

    def cerrar_ventana(self):
        PantallaOE.destroy(self)


