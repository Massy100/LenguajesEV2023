import tkinter as tk
from vistas.vistaCrearAFD import PantallaCrearAFD
from vistas.vistaAyudaAFD import PantallaAyudaAFD

class PantallaAFD(tk.Toplevel):
    pantallaParent=None
    def __init__(self, parent):
        super().__init__()

        self.geometry("640x480")
        self.title("Automata Finito Determinista")

        tk.Button(self, text="Crear AFD", width=100, height=5, command=self.abrir_ventanaCrearAFD).pack(
            expand=True
        )
        tk.Button(self, text="Evaluar Cadena", width=100, height=5).pack(
            expand=True
        )
        tk.Button(self, text="Generar Reporte AFD", width=100, height=5).pack(expand=True)
        tk.Button(self, text="Ayuda", width=100, height=5, command=self.abrir_ventanaAyudaAFD).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)



    def abrir_ventanaCrearAFD(self):
        ventanaCrearAFD = PantallaCrearAFD(self)
        ventanaCrearAFD.grab_set()

    def abrir_ventanaAyudaAFD(self):
        ventanaAyudaAFD = PantallaAyudaAFD(self)
        ventanaAyudaAFD.grab_set()

    def cerrar_ventana(self):
        PantallaAFD.destroy(self)
