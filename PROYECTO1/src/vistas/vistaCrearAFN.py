import tkinter as tk


class PantallaCrearAFN(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.geometry("640x480")
        self.title("Crear Automata Finito No Determinista")

        tk.Label(self, text="Nombre:").pack(expand=True)
        tk.Entry(self).pack(expand=True)

        tk.Label(self, text="Estados:").pack(expand=True)
        tk.Entry(self).pack(expand=True)

        tk.Label(self, text="Alfabeto:").pack(expand=True)
        tk.Entry(self).pack(expand=True)

        tk.Label(self, text="Estado Inicial:").pack(expand=True)
        tk.Entry(self).pack(expand=True)

        tk.Label(self, text="Estados de Aceptacion:").pack(expand=True)
        tk.Entry(self).pack(expand=True)

        tk.Label(self, text="Transiciones:").pack(expand=True)
        tk.Entry(self).pack(expand=True)

        tk.Button(self, text="Guardar", width=100, height=5).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        PantallaCrearAFN.destroy(self)

