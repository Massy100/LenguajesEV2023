import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from itertools import combinations
import graphviz
from PIL import ImageTk, Image
import os

class PantallaSeleccionarAFDOE(tk.Toplevel):
    pantallaParent = None

    def __init__(self, parent):
        super().__init__()
        self.pantallaParent = parent
        self.automataAFD = parent.pantallaParent.automatasCargadosAFD
        self.geometry("640x480")
        self.title("Pantalla Seleccionar AFD")

        tk.Label(self, text="Nombre AFD a Optimizar").pack(expand=True)
        self.automatas = [automata[0] for automata in self.automataAFD]
        self.combobox = ttk.Combobox(self, values=self.automatas)
        self.combobox.pack()

        tk.Label(self, text="Nuevo Nombre para AFD Optimizado").pack(expand=True)
        self.textNombre = tk.Entry(self)
        self.textNombre.pack(expand=True)

        tk.Button(self, text="Aceptar", width=100, height=5,
                  command=self.guardar_automata).pack(expand=True)

        tk.Button(self, text="Regresar", width=100, height=5,
                  command=self.cerrar_ventana).pack(expand=True)

    def guardar_automata(self):
        nuevoNombre=""
        if self.textNombre.get() == "":
            nuevoNombre = self.combobox.get() + "'"
            # Inserta el texto en el Entry
            messagebox.showinfo("Operacion realizada con exito",
                                "El AFD se nombre como el original mas '")
        else:
            nuevoNombre = self.textNombre.get()
            # Inserta el texto en el Entry
            messagebox.showinfo("Operacion realizada con exito",
                                "El AFD se ha guardado exitosamente")
        automataSeleccionado=self.combobox.get()
        for automataAFD in self.pantallaParent.pantallaParent.automatasCargadosAFD:
            if automataAFD[0] == automataSeleccionado:
                self.optimizar_automata(nuevoNombre,automataAFD)

    def cerrar_ventana(self):
        self.destroy()

    def optimizar_automata(self,nuevo_nombre, automata):

        automata_optimizado = self.reducir_AFD(nuevo_nombre,automata[1],automata[2],automata[3],automata[4],automata[5])
        self.pantallaParent.pantallaParent.automatasCargadosAFD_optimizados.append(automata_optimizado)
        print(automata_optimizado[0])
        print(automata_optimizado[1])
        print(automata_optimizado[2])
        print(automata_optimizado[3])
        print(automata_optimizado[4])
        print(automata_optimizado[5])

        tk.Label(self, text= "Nombre: "+automata_optimizado[0]).pack(expand=True)
        tk.Label(self, text= "Estados: "+str(automata_optimizado[1])).pack(expand=True)
        tk.Label(self, text= "Alfabeto: "+str(automata_optimizado[2])).pack(expand=True)
        tk.Label(self, text= "Estado de Inicio:  "+str(automata_optimizado[3])).pack(expand=True)
        tk.Label(self, text= "Estado de Aceptacion: "+str(automata_optimizado[4])).pack(expand=True)
        tk.Label(self, text= "Transiciones: "+str(automata_optimizado[5])).pack(expand=True)

        ventana = tk.Toplevel(self)

        self.geometry("640x480")
        self.title("Pantalla de Automata Finito No Determinista")
        #PantallaCrearAFN.get()
        f = graphviz.Graph()

        # Configuración de la fuente
        f.node_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        f.edge_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        print(automata_optimizado[0])
        print(automata_optimizado[1])
        print(automata_optimizado[2])
        print(automata_optimizado[3])
        print(automata_optimizado[4])
        print(automata_optimizado[5])
        print(automata_optimizado[5][0])
        print(automata_optimizado[5][0][0])
        print(automata_optimizado[5][0][1])
        print(automata_optimizado[5][0][2]) 
    
        #Definición de los nodos del círculo (todo tipo de estado
        f.attr('node', shape = 'circle')
        for estado in automata_optimizado[1]:
            if estado not in automata_optimizado[4]:
                f.node(estado)
            else: #Definición de los nodos dobles circulares (estados de aceptacion)
                f.attr('node', shape ='doublecircle')
                f.node(estado)
                f.attr('node', shape='circle')


        # Definición de las aristas
        #para cada transicion ejecutar: f.edge(estadoInicial, estadoFinal, label = valorTransicion)
        #Lista de transiciones en formato (estado1, valor, estado2), (estado1, valor, estado2) ...
        for transicion in automata_optimizado[5]:
            automata_optimizado[5][0][0], automata_optimizado[5][0][1], automata_optimizado[5][0][2] = transicion
            f.edge(automata_optimizado[5][0][0], automata_optimizado[5][0][2], label=automata_optimizado[5][0][1])


        f.render('automataAFDOptimizado', directory="output", format="png", cleanup=True)
        
        frame = tk.Frame(ventana, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Cargar la imagen
        imagen = Image.open(os.path.join(os.path.dirname(__file__), "../../../output/automataAFDOptimizado.png"))

        # Redimensionar la imagen si es necesario
        imagen = imagen.resize((600, 400))

        # Convertir la imagen a un objeto PhotoImage
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        # Create a Label Widget to display the text or Image
        label = tk.Label(ventana, image = self.imagen_tk)
        label.pack()


    def reducir_AFD(self,nombre,estados, alfabeto, estado_inicial, estados_finales, transiciones):
        # Dividimos los estados en grupos de aceptación y no aceptación
        transiciones_dic = {}
        contador = [0]
        grupo_aceptacion = []
        grupo_no_aceptacion = []
        new_estado_inicial = [estado_inicial]
        new_transicion = []
        new_grupos_aceptacion = []
        new_grupos_no_aceptacion = []
        estado_usado_aceptacion = []
        estado_usado_no_aceptacion = []
        for estado in estados:
            if estado in estados_finales:
                grupo_aceptacion.append(estado)
            else:
                grupo_no_aceptacion.append(estado)

        grupos = [grupo_aceptacion, grupo_no_aceptacion]
        for grupo in grupos:
            self.evaluarPareja(grupo, grupos, alfabeto, transiciones, new_grupos_aceptacion, new_grupos_no_aceptacion,
                      new_estado_inicial, contador, transiciones_dic, estado_usado_aceptacion, estado_usado_no_aceptacion)
        estados_finales = new_grupos_aceptacion
        # Si no formaron parejas quedan en un estado propio
        for estado in grupo_aceptacion:
            if estado not in estado_usado_aceptacion:
                nuevo_nombre = "q"+str(contador[0])
                new_grupos_aceptacion.append(nuevo_nombre)
                transiciones_dic[nuevo_nombre] = [estado]
                contador[0] += 1
        for estado in grupo_no_aceptacion:
            if estado not in estado_usado_no_aceptacion:
                nuevo_nombre = "q"+str(contador[0])
                new_grupos_no_aceptacion.append(nuevo_nombre)
                transiciones_dic[nuevo_nombre] = [estado]
                contador[0] += 1
        self.nuevaTransicion(new_transicion, transiciones_dic, transiciones, alfabeto)
        estados_finales = new_grupos_aceptacion
        estados = [new_grupos_aceptacion+new_grupos_no_aceptacion]
        new_automata=[nombre,estados[0], alfabeto, new_estado_inicial[0], estados_finales, new_transicion]
        return new_automata


    def evaluarPareja(self,grupo_evaluado, grupos, alfabeto, transiciones, new_grupo_aceptacion, new_grupo_no_aceptacion, new_estado_inicial, contador, transiciones_dic, estado_usado_aceptacion, estado_usado_no_aceptacion):
        transiciones_parciales = []
        if (len(grupo_evaluado) > 1):
            parejas = list(combinations(grupo_evaluado, 2))
            for pareja in parejas:
                primero = pareja[0]
                segundo = pareja[1]
                countPair = 0
                for letra in alfabeto:
                    countLetter = 0
                    transicionPrimero = ""
                    transicionSegundo = ""
                    for transicion in transiciones:
                        if (primero == transicion[0] and letra == transicion[1]):
                            countLetter += 1
                            transicionPrimero = transicion[2]
                        if (segundo == transicion[0] and letra == transicion[1]):
                            countLetter += 1
                            transicionSegundo = transicion[2]
                    if (countLetter == 1):
                        countPair += 1
                    elif (countLetter == 2):
                        grupoPrimero = 0
                        grupoSegundo = 0
                        for i, buscarGrupo in enumerate(grupos):
                            if transicionPrimero in buscarGrupo:
                                grupoPrimero = i
                            if transicionSegundo in buscarGrupo:
                                grupoSegundo = i
                        if (grupoPrimero != grupoSegundo):
                            countPair += 1
                if (countPair == 0):
                    nuevo_nombre = "q"+str(contador[0])
                    if (primero == new_estado_inicial[0] or segundo == new_estado_inicial[0]):
                        new_estado_inicial[0] = nuevo_nombre
                    if primero and segundo in grupos[0]:
                        new_grupo_aceptacion.append(nuevo_nombre)
                        estado_usado_aceptacion.append(primero)
                        estado_usado_aceptacion.append(segundo)
                        transiciones_dic[nuevo_nombre] = [primero, segundo]
                        contador[0] += 1
                    else:
                        new_grupo_no_aceptacion.append(nuevo_nombre)
                        estado_usado_no_aceptacion.append(primero)
                        estado_usado_no_aceptacion.append(segundo)
                        transiciones_dic[nuevo_nombre] = [primero, segundo]
                        contador[0] += 1

        else:  # si solo hay uno significa que no se puede reducir
            nuevo_nombre = "q"+str(contador[0])
            if grupo_evaluado[0] in grupos[0]:
                new_grupo_aceptacion.append(nuevo_nombre)
                transiciones_dic[nuevo_nombre] = [grupo_evaluado[0]]
                estado_usado_aceptacion.append(grupo_evaluado[0])
                contador[0] += 1
            else:
                new_grupo_no_aceptacion.append(nuevo_nombre)
                transiciones_dic[nuevo_nombre] = [grupo_evaluado[0]]
                estado_usado_no_aceptacion.append(grupo_evaluado[0])
                contador[0] += 1
            if(grupo_evaluado[0]==new_estado_inicial[0]):
                new_estado_inicial[0]=nuevo_nombre


    def nuevaTransicion(self,new_transicion, transiciones_dic, transiciones, alfabeto):
        for origen, estados in transiciones_dic.items():
            for simbolo in alfabeto:
                destino = None
                for transicion in transiciones:
                    if transicion[0] == estados[0] and transicion[1] == simbolo:
                        destino = [clave for clave, valor in transiciones_dic.items(
                        ) if transicion[2] in valor][0]
                        break
                if destino is not None:
                    transicion = [origen, simbolo, destino]
                    new_transicion.append(transicion)
