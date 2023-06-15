import tkinter as tk
from vistas.vistaAyudaOE import PantallaAyudaOE
from vistas.vistaSeleccionarAFDOE import PantallaSeleccionarAFDOE
from vistas.vistaGenerarOE import PantallaGenerarOE

class PantallaOE(tk.Toplevel):
    pantallaParent=None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFN=parent.automatasCargadosAFD
        self.geometry("640x480")
        self.title("Optimizacion de Estados")

        tk.Button(self, text="Seleccionar AFD", width=100, height=5, command=self.abrir_ventanaSeleccionarAFDOE).pack(
            expand=True
        )
        tk.Button(self, text="Generar Reportes", width=100, height=5, command=self.abrir_ventanaGenerarOE).pack(
            expand=True
        )
        tk.Button(self, text="Ayuda", width=100, height=5, command=self.abrir_ventanaAyudaOE).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def abrir_ventanaAyudaOE(self):
        ventanaAyudaOE = PantallaAyudaOE(self)
        ventanaAyudaOE.grab_set()

    def cerrar_ventana(self):
        PantallaOE.destroy(self)

    def abrir_ventanaSeleccionarAFDOE(self):
        ventanaSeleccionar = PantallaSeleccionarAFDOE(self)
        ventanaSeleccionar.grab_set()

    def abrir_ventanaGenerarOE(self):
        ventanaGenerar = PantallaGenerarOE(self)
        ventanaGenerar.grab_set()
    

