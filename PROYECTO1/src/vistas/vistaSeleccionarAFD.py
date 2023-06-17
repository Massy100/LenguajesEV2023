import tkinter as tk
from tkinter import ttk
from vistas.vistaECAFD import PantallaECAFD

class PantallaSeleccionarAFD(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFD=parent.pantallaParent.automatasCargadosAFD
        self.geometry("640x480")
        self.title("Pantalla Seleccionar AFD")

        automatas = [automata[0] for automata in self.automataAFD]
        self.combobox = ttk.Combobox(self, values=automatas)
        self.combobox.pack()
        tk.Button(self, text="Aceptar", width=100, height=5, command=self.abrir_ventanaECAFD).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        self.destroy()
        
    def abrir_ventanaECAFD(self):
        automataSeleccionado=self.combobox.get()
        for automataAFD in self.pantallaParent.pantallaParent.automatasCargadosAFD:
            if automataAFD[0] == automataSeleccionado:
                ventanaECAFN= PantallaECAFD(self, automataAFD)
                ventanaECAFN.grab_set()
            