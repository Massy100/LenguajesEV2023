import tkinter as tk
from automatas.AFN import AFN
from tkinter import messagebox
import re
import copy

class PantallaCrearAFN(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        
        super().__init__()
        self.pantallaParent=parent
        self.automataAFN=[]
        self.entradas = []
        self.geometry("640x480")
        self.title("Crear Automata Finito No Determinista")

        tk.Label(self, text="Nombre:").pack(expand=True)
        self.textNombre = tk.Entry(self)
        self.textNombre.pack(expand=True)

        tk.Label(self, text="Estados:").pack(expand=True)
        self.textEstados=tk.Entry(self)
        self.textEstados.pack(expand=True)

        tk.Label(self, text="Alfabeto:").pack(expand=True)
        self.textAlfabeto=tk.Entry(self)
        self.textAlfabeto.pack(expand=True)

        tk.Label(self, text="Estado Inicial:").pack(expand=True)
        self.textEstadoInicial=tk.Entry(self)
        self.textEstadoInicial.pack(expand=True)

        tk.Label(self, text="Estados de Aceptacion:").pack(expand=True)
        self.textEstadoAceptacion=tk.Entry(self)
        self.textEstadoAceptacion.pack(expand=True)

        tk.Label(self, text="Transiciones:").pack(expand=True)

        self.frame_transiciones = tk.Frame(self)
        self.frame_transiciones.pack(expand=True)
        
        tk.Button(self, text="Agregar Transicion", width=100, height=5, command=self.crear_entrada).pack(expand=True)
        tk.Button(self, text="Guardar", width=100, height=5, command=self.guardar_automata).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)


    def cerrar_ventana(self):
        self.destroy()

    def crear_entrada(self):
        entrada = tk.Entry(self.frame_transiciones)
        entrada.pack(expand=True)
        self.entradas.append(entrada)
        
    def guardar_automata(self):
        if self.textNombre.get() == "" or self.textEstados.get() == "" or self.textAlfabeto.get() == "" or self.textEstadoInicial.get() == "" or self.textEstadoAceptacion.get() == "" or self.entradas == []:
            print("Alguna entrada está en blanco. Por favor, complete todos los campos.")
        else:
            texto1 = self.textNombre.get()
            texto2 = self.textEstados.get()
            texto3 = self.textAlfabeto.get()
            texto4 = self.textEstadoInicial.get()
            texto5 = self.textEstadoAceptacion.get()
            texto2= texto2.split(",")
            texto3= texto3.split(",")
            texto5= texto5.split(",")
            textos = [entrada.get() for entrada in self.entradas]
            transiciones = [[item for item in texto.replace(';', ',').split(',')] for texto in textos]
            self.automataAFN=[texto1,texto2,texto3,texto4,texto5,transiciones]
<<<<<<< HEAD
            automata_copia = copy.deepcopy(self.automataAFN)
            self.pantallaParent.pantallaParent.automatasCargadosAFN.append(automata_copia)
=======
            self.pantallaParent.pantallaParent.automatasCargadosAFN.append(self.automataAFN)
>>>>>>> 51def8de68bb63400f0fb3c0cd5743c178789658
            '''#Verificar que el estado inicial y los estados de aceptación existan en la lista de estados
            if texto4 not in texto2:
                messagebox.showerror("Error", "El estado inicial no existe en la lista de estados")
                exit()'''
            '''for estado_aceptacion in texto5:
                if estado_aceptacion not in texto2:
                    messagebox.showerror("Error", "Uno o más estados de aceptación no existen en la lista de estados")
                    exit()'''
            '''if "," not in texto2 or "," not in texto3 or ",":
                messagebox.showerror("Error", "Estados o Alfabeto no estan separadas por ','")
                exit()'''

            '''patron = r"^[a-zA-Z], [a-zA-Z], [a-zA-Z]$"
            if re.match(patron, textos):
                print("La transicion cumple con el formato especificado.")
                print("Las transiciones guardadas son:")
                for texto in textos:
                    if texto!="":
                        print(texto)
            else:
                messagebox.showerror("Error", "Alguna transicion no cumple con el formato especificado")'''
                
            instancia = AFN(self.automataAFN) #debe llevar un parametro que tenga el automata




