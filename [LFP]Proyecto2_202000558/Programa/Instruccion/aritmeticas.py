from abst.abstract import Expresion

class Aritmetica(Expresion):
    
    def __init__(self,L ,R , tipo, fila, columna):
        self.L = L
        self.R = R
        self.tipo = tipo
        super().__init__(fila, columna)
        
        
    def operar(self, arbol):
        Lvalue = ''
        Rvalue = ''

        if self.L != None:
            Lvalue = self.L.operar(arbol)
        if self.R != None:
            Rvalue = self.R.operar(arbol)

        if self.tipo.operar(arbol) == 'Suma':
            return Lvalue + Rvalue
        elif self.tipo.operar(arbol) == 'Resta':
            return Lvalue - Rvalue
        elif self.tipo.operar(arbol) == 'Multiplicacion':
            return Lvalue * Rvalue
        elif self.tipo.operar(arbol) == 'Division':
            return Lvalue / Rvalue
        elif self.tipo.operar(arbol) == 'Modulo':
            return Lvalue % Rvalue
        elif self.tipo.operar(arbol) == 'Potencia':
            return Lvalue ** Rvalue
        elif self.tipo.operar(arbol) == 'Raiz':
            return Lvalue ** (1/Rvalue)
        elif self.tipo.operar(arbol) == 'Inverso':
            return 1/Lvalue
        else:
            return 0
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()