from errores import *
from tokn import *
import json

global tokens
global errores

class AnalizadorLexico:
    tokens = []
    errores = []

    def __init__(self):
        self.linea = 1  # Número de línea actual
        self.columna = 1  # Número de columna actual
        self.estado = 0  # Estado actual del autómata
        self.escaner = ''  # almacena el lexema actual
    
    #agregar un error léxico a la lista de errores
    def agregarErrorLexico(self,caracter): 
        global errores
        self.errores.append(ErrorLexico(caracter,self.linea,self.columna))

    # agregar un token a la lista de tokens.
    def agregarToken(self,tipo,token):
        global tokens
        self.tokens.append(Token(tipo,token,self.linea,self.columna))
        self.i -= 1

    def mostar_Tokens(self):
        global tokens
        for token in self.tokens:
            print("|Token |",token.escaner,
            "|Tipo |",token.tipo,
            "|Linea |",token.linea,
            "|Columna |",token.columna)
            
    def mostar_Errores(self):
        global errores
        for error in self.errores:
            print("|Caracter |",error.caracter,
            "|tipo |",error.tipo,
            "|Linea |",error.linea,
            "|Columna |",error.columna)

    def q0(self,caracter):
        if caracter == '-':
            self.estado = 1
            self.columna += 1
            self.escaner += caracter
        elif caracter == '/':
            self.estado = 6
            self.columna += 1
            self.escaner += caracter
        elif caracter.isalpha() or caracter == '$':
            self.estado = 11
            self.columna += 1
            self.escaner += caracter
        elif caracter == '=':
            self.estado = 12
            self.columna += 1
            self.escaner += caracter
        elif caracter == '(':
            self.estado = 13
            self.columna += 1
            self.escaner += caracter
        elif caracter == ')':
            self.estado = 14
            self.columna += 1
            self.escaner += caracter
        elif caracter == ';':
            self.estado = 15
            self.columna += 1
            self.escaner += caracter
        elif caracter == ',':
            self.estado = 16
            self.columna += 1
            self.escaner += caracter
        elif caracter == '"':
            self.estado = 17
            self.columna += 1
            self.escaner += caracter
        elif caracter in [' ']:
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter == ' ':
            pass
        else:
            self.agregarErrorLexico(caracter)
            self.estado = 0
            self.columna += 1
            self.escaner = ''

    def q1(self,caracter):
        if caracter == '-':
            self.estado = 2
            self.columna += 1
            self.escaner += caracter
        else:
            self.agregarError(self.escaner)
            self.estado = 0
            self.columna += 1
            self.escaner = ''

    def q2(self,caracter):
        if caracter == '-':
            self.estado = 3
            self.columna += 1
            self.escaner += caracter
        else:
            self.agregarError(self.escaner)
            self.estado = 0
            self.columna += 1
            self.escaner = ''
            
    def q4(self, caracter):
        if caracter != '\n':
            self.estado = 3
            self.columna += 1
            self.escaner += caracter
        else:
            # reconoce comentario ---
            self.estado = 5
            self.columna = 1
            self.linea += 1

    def q5(self):
        #print(f'Comentario Simple: {self.buffer}')
        self.estado = 0
        self.i -= 1
        self.escaner = ''

    def q6(self,caracter):
        if caracter == '*':
            self.estado = 7
            self.columna += 1
            self.escaner += caracter
        else:
            self.agregarError(self.escaner)
            # self.agregarError(caracter)
            self.estado = 0
            self.columna += 1
            self.escaner = ''

    def q7(self,caracter):
        if caracter != '*':
            self.estado = 8
            self.columna += 1
            self.escaner += caracter
        else:
            self.estado = 9
            self.columna += 1
            self.escaner += caracter

    def q8(self,caracter):
        if caracter != '*':
            self.estado = 8
            self.columna += 1
            self.escaner += caracter
        else:
            self.estado = 9
            self.columna += 1
            self.escaner += caracter

    def q9(self,caracter):
        if caracter != '/':
            self.estado = 8
            self.columna += 1
            self.escaner += caracter
        else:
            self.estado = 10
            self.columna += 1
            self.escaner += caracter

    def q10(self):
        #print(f'Comentario Multilinea: {self.buffer}')
        self.estado = 0
        self.i -= 1
        self.escaner = ''

    def q11(self,caracter):
        if caracter.isalnum():
            self.estado = 11
            self.columna += 1
            self.escaner += caracter
        else:
            if self.escaner in ['CrearBD','EliminarBD','CrearColeccion','EliminarColeccion','InsertarUnico','ActualizarUnico','EliminarUnico','BuscarTodo','BuscarUnico','nueva']:
                self.agregarToken(f'RESERVADA',self.escaner)
                self.escaner = ''
                self.estado = 0
            else:
                self.agregarToken('IDENTIFICADOR',self.escaner)
                self.escaner = ''
                self.estado = 0

    def agregarSimbolo(self):
        self.agregarToken('SIMBOLO', self.escaner)
        self.escaner = ''
        self.estado = 0
        
    def q12(self):
        self.agregarSimbolo()

    def q13(self,caracter):
        if caracter != '"':
            if caracter == '\t' or caracter == '\n':
                self.estado = 17
                self.linea += 1
                self.columna = 1
            elif caracter == '{':
                self.estado = 20
                self.escaner = caracter
            else:
                self.estado = 18
                self.escaner += caracter
            self.columna += 1
        else:
            self.estado = 19
            self.columna += 1
            self.escaner += caracter

    def q14(self,caracter):
        if caracter != '"':
            self.estado = 18
            self.columna += 1
            self.escaner += caracter
        else:
            self.estado = 19
            self.columna += 1
            self.escaner += caracter

    def q15(self):
        self.agregarToken('IDENTIFICADOR',self.escaner)
        self.escaner = ''
        self.estado = 0

    def q16(self,caracter):
        if caracter != '}':
            self.estado = 21
            if caracter == '\n':
                self.columna = 1
                self.linea += 1
            else:
                self.columna += 1
                self.escaner += caracter
        else:
            self.estado = 22
            self.columna += 1
            self.escaner += caracter

    def q17(self,caracter):
        if caracter != ')':
            self.estado = 21
            if caracter == '\n':
                self.columna = 1
                self.linea += 1
            else:
                self.columna += 1
                self.escaner += caracter
        else:
            self.estado = 22
            self.columna += 1

    def q18(self):
        try:
            self.escaner = self.escaner[:-1]
        except: pass
        self.agregarToken('JSON',self.escaner)
        self.escaner = ''
        self.estado = 0
        self.i -= 1

    def analizar(self,cadena):
        cadena += '\n'
        self.i = 0
        while(self.i < len(cadena)):
            if self.estado == 0:
                self.q0(cadena[self.i])
            elif self.estado == 1:
                self.q1(cadena[self.i])
            elif self.estado == 2:
                self.q2(cadena[self.i])
            elif self.estado == 3 or self.estado == 4:
                self.q4(cadena[self.i])
            elif self.estado == 5:
                self.q5()
            elif self.estado == 6:
                self.q6(cadena[self.i])
            elif self.estado == 7:
                self.q7(cadena[self.i])
            elif self.estado == 8:
                self.q8(cadena[self.i])
            elif self.estado == 9:
                self.q9(cadena[self.i])
            elif self.estado == 10:
                self.q10()
            elif self.estado == 11:
                self.q11(cadena[self.i])
            elif self.estado == 12 or self.estado == 13 or self.estado == 14 or self.estado == 15 or self.estado == 16 :
                self.q12()
            elif self.estado == 17:
                self.q13(cadena[self.i])
            elif self.estado == 18:
                self.q14(cadena[self.i])
            elif self.estado == 19:
                self.q15()
            elif self.estado == 20:
                self.q16(cadena[self.i])
            elif self.estado == 21:
                self.q17(cadena[self.i])
            elif self.estado == 22:
                self.q18()
            self.i += 1

    def limpiarLista(self):
        global tokens
        global errores
        
        tokens = []
        errores = []

    def analizarS(self, cadena):
        self.tokens = []
        for linea in cadena.split("\n"):
            linea = linea.strip()
            if not linea:
                continue
            tokens = linea.split()
            self.tokens.append(tokens)

    def generar(self, cadena):
        self.analizarS(cadena)
        sentencias = []
        for tokens in self.tokens:
            if tokens[0] == "CrearBD":
                sentencias.append(f"use('{tokens[1]}');")
            elif tokens[0] == "CrearColeccion":
                sentencias.append(f"db.createCollection('{tokens[1]}');")
            elif tokens[0] == "InsertarUnico":
                nombre_coleccion = tokens[1]
                documento = tokens[2][1:1]
                sentencias.append(f"db.{nombre_coleccion}.insertOne({documento});")
            elif tokens[0] == "EliminarColeccion":
                sentencias.append(f"db.{tokens[1]}.drop();")
            elif tokens[0] == "ActualizarUnico":
                nombre_coleccion = tokens[1]
                filtro = tokens[2][1:1]
                cambio = tokens[3][1:1]
                sentencias.append(f"db.{nombre_coleccion}.updateOne({filtro}, {cambio});")
            elif tokens[0] == "EliminarUnico":
                nombre_coleccion = tokens[1]
                filtro = tokens[2][1:1]
                sentencias.append(f"db.{nombre_coleccion}.deleteOne({filtro});")
            elif tokens[0] == "BuscarTodo":
                sentencias.append(f"db.{tokens[1]}.find();")
        resultado = "\n".join(sentencias)
        return print(resultado)
    

contenido = '''
CrearBD cali = nueva CrearBD();
CrearColeccion colec = nueva CrearColeccion("Coleccion1");
CrearColeccion colec2 = nueva CrearColeccion("Coleccion2");
CrearColeccion colec3 = nueva CrearColeccion("Coleccion3");
InsertarUnico uno = nueva InsertarUnico("Coleccion1",
"
	{
		"id": 1,
		"nombre": "Calificacion 1",
		"anio": 2023,
		"curso": "Lenguajes Formales y de Programacion"
	}
");

InsertarUnico dos = nueva InsertarUnico("Coleccion1",
"
	{
		"id": 1,
		"nombre": "Calificacion 2",
		"anio": 2023,
		"curso": "Introduccion a la Programacion 2"
	}
");

**
EliminarColeccion c1 = nueva EliminarColeccion("Coleccion2");

ActualizarUnico ac1 = nueva ActualizarUnico("Coleccion1",
"
	{
		"id" : 1
	},
	{
		$set: {"curso": "Oficialmente estoy en Compi 1"}
	}
"
);


EliminarUnico el1 = nueva EliminarUnico("Coleccion1",
"
	{
		"id" : 2
	}

"*
);


BuscarTodo todo = nueva BuscarTodo("Coleccion1");
'''
#lexico = AnalizadorLexico()
#lexico.analizar(contenido)
#lexico.mostar_Errores()
#lexico.mostar_Tokens()
#lexico.generar(contenido)