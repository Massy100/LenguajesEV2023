import tkinter as tk
from vistas.vistaCrearAFN import PantallaCrearAFN
from vistas.vistaAyudaAFN import PantallaAyudaAFN


class PantallaAFN(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.geometry("640x480")
        self.title("Automata Finito No Determinista")

        tk.Button(self, text="Crear AFN", width=100, height=5, command=self.abrir_ventanaCrearAFN).pack(
            expand=True
        )
        tk.Button(self, text="Evaluar Cadena", width=100, height=5).pack(
            expand=True
        )
        tk.Button(self, text="Generar Reporte AFN", width=100, height=5).pack(expand=True)
        tk.Button(self, text="Ayuda", width=100, height=5, command=self.abrir_ventanaAyudaAFN).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def abrir_ventanaCrearAFN(self):
        ventanaCrearAFN = PantallaCrearAFN(self)
        ventanaCrearAFN.grab_set()

    def abrir_ventanaAyudaAFN(self):
        ventanaAyudaAFN = PantallaAyudaAFN(self)
        ventanaAyudaAFN.grab_set()

    def cerrar_ventana(self):
        PantallaAFN.destroy(self)

