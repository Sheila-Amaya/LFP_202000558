class Token:
    def __init__(self,tipo,escaner,linea,columna):
        self.tipo = tipo
        self.escaner = escaner
        self.linea = linea
        self.columna = columna