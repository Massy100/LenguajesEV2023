import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
from PIL import ImageTk, Image
import os

class PantallaGenerarOE(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFD=parent.pantallaParent.automatasCargadosAFD_optimizados
        self.geometry("640x480")
        self.title("Pantalla Generar Reporte OE")

        tk.Label(self, text="Seleccione un AFD").pack(expand=True)
        automatas = [automata[0] for automata in self.automataAFD]
        self.combobox = ttk.Combobox(self, values=automatas)
        self.combobox.pack()

        tk.Button(self, text="Aceptar", width=100, height=5, command=self.generarPDF).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        self.destroy()

    def generarPDF(self):
        automataSeleccionado=self.combobox.get()
        for automataAFD in self.pantallaParent.pantallaParent.automatasCargadosAFD_optimizados:
            if automataAFD[0] == automataSeleccionado:
                automataSeleccionado=automataAFD
                break
        w, h = A4
        pdf = canvas.Canvas("ReporteAFDOptimizado.pdf", pagesize=A4)
        pdf.setTitle("Reporte de AFD Optimizado")
        text = pdf.beginText(50, h-50)
        text.setFont("Times-Roman", 12)
        text.textLine("Nombre:"+automataSeleccionado[0])
        text.textLine("Estados: "+str(automataSeleccionado[1]))
        text.textLine("Alfabeto: "+str(automataSeleccionado[2]))
        text.textLine("Estado Inicial: "+str(automataSeleccionado[3]))
        text.textLine("Estado de Aceptacion: "+str(automataSeleccionado[4]))
        text.textLine("Transiciones: "+str(automataSeleccionado[5]))
        try :
            text.textLine("Cadena Generada: "+self.generarCadena())
        except:
            text.textLine("Cadena Generada: ")
        text.textLine()
        text.textLine("AFD Original:")
        text.textLine("AFD Optimizado:")
        pdf.drawText(text)
        pdf.drawInlineImage("output/"+automataSeleccionado[6]+".png", 0,h-400, width=200, height=200, preserveAspectRatio=True)
        pdf.drawInlineImage("output/"+automataSeleccionado[0]+".png", 0,h-800, width=200, height=200, preserveAspectRatio=True)
        pdf.save()
        webbrowser.open_new_tab('ReporteAFDOptimizado.pdf')

    def generarCadena(self):
        automataSeleccionado=self.combobox.get()
        for automataAFD in self.pantallaParent.pantallaParent.automatasCargadosAFD:
            if automataAFD[0] == automataSeleccionado:
                automataSeleccionado=automataAFD
                break
        cadenaGenerada=""
        transicionInicial=None
        cadenaValida = False
        #Se busca una transicion inicial
        for transicion in automataSeleccionado[5]:
            if transicion[0] == automataSeleccionado[3]:
                transicionInicial = transicion
                break
        transicionActual = transicionInicial
        #Si mi transicion inicial ya contiene un estado de aceptacion no se hace nada mas
        if transicionActual[2] not in automataSeleccionado[4]:
            #Se recorren todas las transiciones una y otra vez
            #hasta obtener una cadena valida
            while True:
                for transicion in automataSeleccionado[5]:
                    #Si mi estado de destino actual es igual a el estado origen
                    #de la transicion siguiente se mueve a esa transicion
                    if transicion[0] == transicionActual[2]:
                        #Si el estado destino de la siguiente transicion es igual a
                        #mi estado origen actual (transicion circular)
                        #se omite
                        if transicion[2] == transicionActual[0]:
                            continue
                        #Si la transicion siguiente me lleva al estado actual
                        if transicion[0] == transicion[2]:
                            continue
                        #Se mueve a la siguiente transicion y agrega el caracter
                        #con el que la transicion actual se mueve a la cadena generada
                        #Si el estado destino de la transicion actual es un estado de aceptacion
                        #se marca la cadena como valida
                        if transicionActual[2] in automataSeleccionado[4]:
                            cadenaValida = True
                            break
                if cadenaValida:
                    break
        return cadenaGenerada
        