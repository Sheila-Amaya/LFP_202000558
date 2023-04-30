from errores import *
from tokn import *
import json

global tokens
global errores

class AnalizadorLexico:
    tokens = []
    errores = []

    def __init__(self):
        self.linea = 1
        self.columna = 1
        self.estado = 0
        self.buffer = ''

    def agregarErrorLexico(self,caracter):
        global errores
        self.errores.append(ErrorLexico(caracter,self.linea,self.columna))

    def agregarToken(self,tipo,token):
        global tokens
        self.tokens.append(Token(tipo,token,self.linea,self.columna))
        self.i -= 1
        
    def mostar_Tokens(self):
        global tokens
        for token in self.tokens:
            print("|Token |",token.buffer,
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
            self.buffer += caracter
        elif caracter == '/':
            self.estado = 6
            self.columna += 1
            self.buffer += caracter
        elif caracter.isalpha() or caracter == '$':
            self.estado = 11
            self.columna += 1
            self.buffer += caracter
        elif caracter == '=':
            self.estado = 12
            self.columna += 1
            self.buffer += caracter
        elif caracter == '(':
            self.estado = 13
            self.columna += 1
            self.buffer += caracter
        elif caracter == ')':
            self.estado = 14
            self.columna += 1
            self.buffer += caracter
        elif caracter == ';':
            self.estado = 15
            self.columna += 1
            self.buffer += caracter
        elif caracter == ',':
            self.estado = 16
            self.columna += 1
            self.buffer += caracter
        elif caracter == '"':
            self.estado = 17
            self.columna += 1
            self.buffer += caracter
        elif caracter in [' ']:
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter == '':
            pass
        else:
            self.agregarErrorLexico(caracter)
            self.estado = 0
            self.columna += 1
            self.buffer = ''

    def q1(self,caracter):
        if caracter == '-':
            self.estado = 2
            self.columna += 1
            self.buffer += caracter
        else:
            self.agregarErrorLexico(self.buffer)
            self.estado = 0
            self.columna += 1
            self.buffer = ''

    def q2(self,caracter):
        if caracter == '-':
            self.estado = 3
            self.columna += 1
            self.buffer += caracter
        else:
            self.agregarErrorLexico(self.buffer)
            self.estado = 0
            self.columna += 1
            self.buffer = ''
            
    def q3(self, caracter):
        if caracter != '\n':
            self.estado = 3
            self.columna += 1
            self.buffer += caracter
        else:
            # reconoce comentario ---
            self.estado = 5
            self.columna = 1
            self.linea += 1

    def q4(self):
        #print(f'Comentario Simple: {self.buffer}')
        self.estado = 0
        self.i -= 1
        self.buffer = ''

    def q5(self,caracter):
        if caracter == '*':
            self.estado = 7
            self.columna += 1
            self.buffer += caracter
        else:
            self.agregarErrorLexico(self.buffer)
            # self.agregarError(caracter)
            self.estado = 0
            self.columna += 1
            self.buffer = ''

    def q6(self,caracter):
        if caracter != '*':
            self.estado = 8
            self.columna += 1
            self.buffer += caracter
        else:
            self.estado = 9
            self.columna += 1
            self.buffer += caracter

    def q7(self,caracter):
        if caracter != '*':
            self.estado = 8
            self.columna += 1
            self.buffer += caracter
        else:
            self.estado = 9
            self.columna += 1
            self.buffer += caracter

    def q8(self,caracter):
        if caracter != '/':
            self.estado = 8
            self.columna += 1
            self.buffer += caracter
        else:
            self.estado = 10
            self.columna += 1
            self.buffer += caracter

    def q9(self):
        #print(f'Comentario Multilinea: {self.buffer}')
        self.estado = 0
        self.i -= 1
        self.buffer = ''

    def q10(self,caracter):
        if caracter.isalnum():
            self.estado = 11
            self.columna += 1
            self.buffer += caracter
        else:
            if self.buffer in ['CrearBD','EliminarBD','CrearColeccion','EliminarColeccion','InsertarUnico','ActualizarUnico','EliminarUnico','BuscarTodo','BuscarUnico','nueva']:
                self.agregarToken(f'RESERVADA',self.buffer)
                self.buffer = ''
                self.estado = 0
            else:
                self.agregarToken('IDENTIFICADOR',self.buffer)
                self.buffer = ''
                self.estado = 0

    def agregarSimbolo(self):
        self.agregarToken('SIMBOLO', self.buffer)
        self.buffer = ''
        self.estado = 0
        
    def q11(self):
        self.agregarSimbolo()

    def q12(self,caracter):
        if caracter != '"':
            if caracter == '\n':
                self.estado = 17
                self.linea += 1
                self.columna = 1
            elif caracter == '{':
                self.estado = 20
                self.buffer = caracter
            else:
                self.estado = 18
                self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 19
            self.columna += 1
            self.buffer += caracter

    def q13(self,caracter):
        if caracter != '"':
            self.estado = 18
            self.columna += 1
            self.buffer += caracter
        else:
            self.estado = 19
            self.columna += 1
            self.buffer += caracter

    def q14(self):
        self.agregarToken('cadena',self.buffer)
        self.buffer = ''
        self.estado = 0

    def q15(self,caracter):
        if caracter != '}':
            self.estado = 21
            if caracter == '\n':
                self.columna = 1
                self.linea += 1
            else:
                self.columna += 1
                self.buffer += caracter
        else:
            self.estado = 22
            self.columna += 1
            self.buffer += caracter

    def q16(self,caracter):
        if caracter != ')':
            self.estado = 21
            if caracter == '\n':
                self.columna = 1
                self.linea += 1
            else:
                self.columna += 1
                self.buffer += caracter
        else:
            self.estado = 22
            self.columna += 1

    def q17(self):
        try:
            self.buffer = self.buffer[:-1]
        except: pass
        self.agregarToken('dato',self.buffer)
        self.buffer = ''
        self.estado = 0
        self.i -= 1


    def analizar (self,cadena):
        cadena += '\n#'
        self.i = 0
        while(self.i < len(cadena)):
            if self.estado == 0:
                self.q0(cadena[self.i])
            elif self.estado == 1:
                self.q1(cadena[self.i])
            elif self.estado == 2:
                self.q2(cadena[self.i])
            elif self.estado == 3:
                self.q3(cadena[self.i])
            elif self.estado == 4:
                self.q3(cadena[self.i])
            elif self.estado == 5:
                self.q4()
            elif self.estado == 6:
                self.q5(cadena[self.i])
            elif self.estado == 7:
                self.q6(cadena[self.i])
            elif self.estado == 8:
                self.q7(cadena[self.i])
            elif self.estado == 9:
                self.q8(cadena[self.i])
            elif self.estado == 10:
                self.q9()
            elif self.estado == 11:
                self.q10(cadena[self.i])
            elif self.estado == 12:
                self.q11()
            elif self.estado == 13:
                self.q11()
            elif self.estado == 14:
                self.q11()
            elif self.estado == 15:
                self.q11()
            elif self.estado == 16:
                self.q11()
            elif self.estado == 17:
                self.q12(cadena[self.i])
            elif self.estado == 18:
                self.q13(cadena[self.i])
            elif self.estado == 19:
                self.q14()
            elif self.estado == 20:
                self.q15(cadena[self.i])
            elif self.estado == 21:
                self.q16(cadena[self.i])
            elif self.estado == 22:
                self.q17()
            self.i += 1
            
    def generarSentencias(self):
                    pass
                
    def limpiarLista(self):
        global tokens
        global errores
        
        tokens = []
        errores = []

contenido = '''

/* 
	ARCHIVO DE PRUEBAS 
	CON COMENTARIOS
*/


--- CREAR BASE DE DATOS
CrearBD temp1 = nueva CrearBD();

--- ELIMINAR BASE DE DATOS
EliminarBD temp1 = nueva EliminarBD();

/* 
	BASE DE DATOS DE  LITERATURAS
*/

--- CREAR BASE DE DATOS
CrearBD temp = nueva CrearBD();

--- CREAR COLECCION DE LITERATURAS
CrearColeccion colec = nueva CrearColeccion(“literaturas”);

--- CREAR COLECCION TEMPORAL
CrearColeccion colec = nueva CrearColeccion(“colectemp”);

--- ELIMINAR COLECCION TEMPORAL
EliminarColeccion eliminacolec = nueva EliminarColeccion(“colectemp”);

/* 
	INSERTAR DATOS
*/
InsertarUnico insert1 = nueva InsertarUnico(“literaturas” ,
“
{
 "nombre" : "Obra Literaria",
 "autor" : "Jorge Luis"
 }
”);

InsertarUnico insert2 = nueva InsertarUnico(“literaturas” ,
“
{
 "nombre" : "El Principito",
 "autor" : "Antoine de Saint"
 }
”);

InsertarUnico insert3 = nueva InsertarUnico(“literaturas” ,
“
{
 "nombre" : "Moldavita. Un Visitante Amigable",
 "autor" : "Norma Muñoz Ledo"
 }
”);

--- ACTUALIZAR DATO DE COLECCION LITERATURA
ActualizarUnico actualizadoc = nueva ActualizarUnico(“literaturas”,
“
{
 "nombre" : "Obra Literaria"
},
{
 $set: {"autor" : "Mario Vargas"}
}
”);

--- ELIMINAR DATO DE LA COLECCION LITERATURA
EliminarUnico eliminadoc = nueva EliminarUnico(“literaturas”,
“
{
 "nombre" : "Obra Literaria"
}
”);

--- BUSCAR TODOS LOS DATOS DE LA COLECCION
BuscarTodo todo = nueva BuscarTodo (“literaturas”);

--- BUSCAR UN DATO POR COLECCION
BuscarUnico todo = nueva BuscarUnico (“literaturas”);
'''

#lexico = AnalizadorLexico()
#lexico.analizar(contenido)
#lexico.mostar_Tokens()
#lexico.limpiarLista()
#lexico.mostar_Tokens() ,print("hola")
#lexico.mostar_Errores()