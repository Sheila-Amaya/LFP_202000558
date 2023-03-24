from abst.abstract import Expresion

class Aritmetica(Expresion):
    
    def __init__(self,L ,R , tipo, fila, columna):
        self.L = L
        self.R = R
        self.tipo = tipo
        self.valor = ""
        super().__init__(fila, columna)
        
        
    def operar(self, arbol):
        Lvalue = ''
        Rvalue = ''

        if self.L != None:
            Lvalue = self.L.operar(arbol)
        if self.R != None:
            Rvalue = self.R.operar(arbol)

        if self.tipo.operar(arbol) == 'Suma':
            resultado = Lvalue + Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Resta':
            resultado = Lvalue - Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Multiplicacion':
            resultado = Lvalue * Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Division':
            resultado =  Lvalue / Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Modulo':
            resultado =  Lvalue % Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Potencia':
            resultado =  Lvalue ** Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Raiz':
            resultado =  Lvalue ** (1/Rvalue)
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Inverso':
            resultado =  1/Lvalue
            self.valor = resultado
            return resultado
        else:
            return 0
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()