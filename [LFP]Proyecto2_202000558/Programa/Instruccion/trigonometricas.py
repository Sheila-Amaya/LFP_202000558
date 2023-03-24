from abst.abstract import Expresion
from math import *

class Trigonometrica(Expresion):
    
    def __init__(self, L, tipo, fila, columna):
        self.L = L
        self.tipo = tipo
        self.valor = ""
        super().__init__(fila, columna)
        
        
    def operar(self, arbol):
        Lvalue = ''

        if self.L != None:
            Lvalue = self.L.operar(arbol)
            
        if self.tipo.operar(arbol) == 'Seno':
            resultado = sin(Lvalue)
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Coseno':
            resultado = cos(Lvalue)
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Tangente':
            resultado = tan(Lvalue)
            self.valor = resultado
            return resultado
        else:
            return 0
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()