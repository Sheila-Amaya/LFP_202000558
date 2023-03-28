from abst.abstract import Expresion

class Lexema(Expresion):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.lexema
    
    def getFila(self):
        return super().getFila() #llama al constructor de la clase base y pasa los valores de f y c
    
    def getColumna(self):
        return super().getColumna()
    
    def get_valor(self):
        return self.lexema