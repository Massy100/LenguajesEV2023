class DataAFD():
    def __init__(self):
        self.estados = []
        self.alfabeto = []
        self.estado_inicial = None
        self.estados_de_aceptacion=[]
        self.transiciones=[]

class TransicionesAFD():
    def __init__(self, estado_inicial, valor_transicion, estado_final):
        self.estado_inicial = estado_inicial
        self.valor_transicion = valor_transicion
        self.estado_final = estado_final
    def transform(self):
        return [self.estado_final,self.valor_transicion,self.estado_final]