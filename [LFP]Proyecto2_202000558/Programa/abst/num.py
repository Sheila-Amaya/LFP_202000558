from abst.abstract import Expresion

class Num(Expresion):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        super().__init__(fila, columna)
        
    def operar(self, arbol):
        return self.valor
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
    
    def get_valor(self):
        return self.valor