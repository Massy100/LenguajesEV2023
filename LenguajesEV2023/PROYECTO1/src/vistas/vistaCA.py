import tkinter as tk
from tkinter import filedialog
from automatas.DataAFD import DataAFD, TransicionesAFD
from automatas.DataAFN import DataAFN, TransicionesAFN


class PantallaCA(tk.Toplevel):
    pantallaParent=None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent

        self.geometry("640x480")
        self.title("Carga de Archivos")

        tk.Button(self, text="Cargar AFD", width=100, height=5, command = self.cargarAFD).pack(
            expand=True
        )
        tk.Button(self, text="Cargar AFN", width=100, height=5, command = self.cargarAFN).pack(
            expand=True
        )
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        PantallaCA.destroy(self)

    def cargarAFD(self):
        automatasAFD = []
        automataActual=None
        dataAutomataActual=None
        estadoAutomata=None
        alfabetoAutomata=None
        estadoInicialAutomata=None
        estadoAceptacionAutomata=None
        
        nombre_archivo = filedialog.askopenfilename(filetypes=[("Todos los archivos", "*.afd")])
        with open(nombre_archivo, "r") as archivo:
            contador = 0
            for linea in archivo:
                linea = linea.rstrip()
                #print(linea)
                contador += 1
                if contador==1:
                    automataActual=linea
                    dataAutomataActual=DataAFD()
                elif contador==2:
                    estados=linea.split(",")
                    for state in estados:
                        dataAutomataActual.estados.append(state)
                elif contador==3:
                    alfabeto=linea.split(",")
                    for alfabet in alfabeto:
                        dataAutomataActual.alfabeto.append(alfabet)
                elif contador==4:
                    estadoInicialAutomata=linea
                    dataAutomataActual.estado_inicial=estadoInicialAutomata
                elif contador==5:
                    estadoAceptacion=linea.split(",")
                    for stateAcept in estadoAceptacion:
                        dataAutomataActual.estados_de_aceptacion.append(stateAcept)
                if(";" in linea):
                    #encontramos una transicion porque hay un ;
                    linea = linea.replace(";", ",")
                    estados=linea.split(",")
                    transicionActual=TransicionesAFD(estados[0], estados[1], estados[2]).transform()
                    dataAutomataActual.transiciones.append(transicionActual)
                """ elif("," in linea):
                    print("Mostrar separacion")
                    estados=linea.split(",")
                    for estado in estados:
                        print(estado)
                    print("Fin separacion") """
                if("%" in linea):
                    automatasAFD.append((automataActual, dataAutomataActual.estados,dataAutomataActual.alfabeto,dataAutomataActual.estado_inicial,dataAutomataActual.estados_de_aceptacion,dataAutomataActual.transiciones))
                    contador=0
                    automataActual=None
                    dataAutomataActual=None
                    estadoAutomata=None
                    alfabetoAutomata=None
                    estadoInicialAutomata=None
                    estadoAceptacionAutomata=None

        self.pantallaParent.automatasCargadosAFD.extend(automatasAFD)
        arrayAutomatas=automatasAFD
        print("se cargo afd")
        #[automata][(0-nombre)(1-estados)(2-alfabeto)(3-estado_inicial)(4-estado_de_aceptacion)(5-transiciones)]
        print(arrayAutomatas[0][0])
        print(arrayAutomatas[0][1])
        #[automata][estados][posicionQueQuieres ej: (0-primeraPosicion)]
        print(arrayAutomatas[0][1][0])
        print(arrayAutomatas[0][2])
        #[automata][alfabeto][posicionQueQuieres ej: (0-primeraPosicion)]
        print(arrayAutomatas[0][2][0])
        print(arrayAutomatas[0][3])
        #[automata][alfabeto][posicionQueQuieres ej: (0-primeraPosicion)]
        print(arrayAutomatas[0][4])
        print(arrayAutomatas[0][4][0])
        print(arrayAutomatas[0][5])
        #[automata][transicion(5)][valor-0(primeraTransicion)]
        print(arrayAutomatas[0][5][0])
        #[automata][transicion][posicionTransicion(0-primeraTransicion)][posicionDeTransicion(0-estadoInicial,1-valorTransicion,2-estadoFinal)]
        print(arrayAutomatas[0][5][0][0])
        print(arrayAutomatas[0][5][0][1])
        print(arrayAutomatas[0][5][0][2])
        #automatas.items()
        """ for nombre, infoAutomata in automatas.items():
            print(nombre)
            print(count)
            print(infoAutomata.estados)
            print(infoAutomata.alfabeto)
            print(infoAutomata.estado_inicial)
            print(infoAutomata.estados_de_aceptacion)
            [print(obj.__dict__) for obj in infoAutomata.transiciones] """

    def cargarAFN(self):
        automatasAFN = []
        automataActual=None
        dataAutomataActual=None
        estadoAutomata=None
        alfabetoAutomata=None
        estadoInicialAutomata=None
        estadoAceptacionAutomata=None
        
        nombre_archivo = filedialog.askopenfilename(filetypes=[("Todos los archivos", "*.afn")])
        with open(nombre_archivo, "r") as archivo:
            contador = 0
            for linea in archivo:
                linea = linea.rstrip()
                #print(linea)
                contador += 1
                if contador==1:
                    automataActual=linea
                    dataAutomataActual=DataAFN()
                elif contador==2:
                    estados=linea.split(",")
                    for state in estados:
                        dataAutomataActual.estados.append(state)
                elif contador==3:
                    alfabeto=linea.split(",")
                    for alfabet in alfabeto:
                        dataAutomataActual.alfabeto.append(alfabet)
                elif contador==4:
                    estadoInicialAutomata=linea
                    dataAutomataActual.estado_inicial=estadoInicialAutomata
                elif contador==5:
                    estadoAceptacion=linea.split(",")
                    for stateAcept in estadoAceptacion:
                        dataAutomataActual.estados_de_aceptacion.append(stateAcept)
                if(";" in linea):
                    #encontramos una transicion porque hay un ;
                    linea = linea.replace(";", ",")
                    estados=linea.split(",")
                    transicionActual=TransicionesAFN(estados[0], estados[1], estados[2]).transform()
                    dataAutomataActual.transiciones.append(transicionActual)
                """ elif("," in linea): 
                    print("Mostrar separacion")
                    estados=linea.split(",")
                    for estado in estados:
                        print(estado)
                    print("Fin separacion") """
                if("%" in linea):
                    automatasAFN.append((automataActual, dataAutomataActual.estados,dataAutomataActual.alfabeto,dataAutomataActual.estado_inicial,dataAutomataActual.estados_de_aceptacion,dataAutomataActual.transiciones))
                    contador=0
                    automataActual=None
                    dataAutomataActual=None
                    estadoAutomata=None
                    alfabetoAutomata=None
                    estadoInicialAutomata=None
                    estadoAceptacionAutomata=None

        self.pantallaParent.automatasCargadosAFN.extend(automatasAFN) #aqui se cargan los automatas al parent
        arrayAutomatas=automatasAFN
        print("Se guarda AFN")
        print(self.pantallaParent.automatasCargadosAFN.__len__())
        '''#[automata][(0-nombre)(1-estados)(2-alfabeto)(3-estado_inicial)(4-estado_de_aceptacion)(5-transiciones)]
        print(arrayAutomatas[0][0])
        print(arrayAutomatas[0][1])
        #[automata][estados][posicionQueQuieres ej: (0-primeraPosicion)]
        print(arrayAutomatas[0][1][0])
        print(arrayAutomatas[0][2])
        #[automata][alfabeto][posicionQueQuieres ej: (0-primeraPosicion)]
        print(arrayAutomatas[0][2][0])
        print(arrayAutomatas[0][3])
        #[automata][alfabeto][posicionQueQuieres ej: (0-primeraPosicion)]
        print(arrayAutomatas[0][4])
        print(arrayAutomatas[0][4][0])
        print(arrayAutomatas[0][5])
        #[automata][transicion(5)][valor-0(primeraTransicion)]
        print(arrayAutomatas[0][5][0])
        #[automata][transicion][posicionTransicion(0-primeraTransicion)][posicionDeTransicion(0-estadoInicial,1-valorTransicion,2-estadoFinal)]
        print(arrayAutomatas[0][5][0][0])
        print(arrayAutomatas[0][5][0][1])
        print(arrayAutomatas[0][5][0][2])
        #automatas.items()'''
        """ for nombre, infoAutomata in automatas.items():
            print(nombre)
            print(count)
            print(infoAutomata.estados)
            print(infoAutomata.alfabeto)
            print(infoAutomata.estado_inicial)
            print(infoAutomata.estados_de_aceptacion)
            [print(obj.__dict__) for obj in infoAutomata.transiciones] """



