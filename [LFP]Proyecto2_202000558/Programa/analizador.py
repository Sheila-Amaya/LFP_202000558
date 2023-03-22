from Instruccion.aritmeticas import *
from Instruccion.trigonometricas import *
from abst.lexema import *
from abst.num import *
from errores import *
import json
import os



#palabras reservadas son los lexemas
#token | lexema
reservadas = {
    'ROPERACION'        :   'Operacion',
    'RVALOR1'           :   'Valor1',
    'RVALOR2'           :   'Valor2',
    'RSUMA'             :   'Suma',
    'RRESTA'            :   'Resta',
    'RMULTIPLICACION'   :   'Multiplicacion',
    'RDIVISION'         :   'Division',
    'RPOTENCIA'         :   'Potencia',
    'RRAIZ'             :   'Raiz',
    'RINVERSO'          :   'Inverso',
    'RSENO'             :   'Seno',
    'RCOSENO'           :   'Coseno',
    'RTANGENTE'         :   'Tangente',
    'RMOD'              :   'Mod',
    'RTEXTO'            :   'Texto',
    'RCOLORFONDONODO'   :   'Color-Fondo-Nodo',
    'RCOLORFUENTENODO'  :   'Color-Fuente-Nodo',
    'RFORMANODO'        :   'Forma-Nodo',
    'COMA'              :   ',',
    'PUNTO'             :   '.',
    'DPUNTO'            :   ':',
    'CORI'              :   '[',
    'CORD'              :   ']',
    'LLAVEI'            :   '}',
    'LLAVED'            :   '{',
}

Lexemas = list(reservadas.values())
global n_linea
global n_columna
global instrucciones
global lista_lexema
global lista_errores

n_linea = 1
n_columna = 1
lista_lexema = []
instrucciones = []
lista_errores = []


def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexema
    global lista_errores
    
    pos = 0

    lexema = ''
    puntero = 0
    
    while cadena:
        char = cadena[puntero]
        puntero += 1
        

        if char == '\"':
            lexema, cadena = armar_Lexema(cadena[puntero:])
            if lexema and cadena: 
                n_columna +=1
                #arma el lexema
                l = Lexema(lexema, n_linea, n_columna)
                
                lista_lexema.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
        
        elif char.isdigit():
            token,  cadena = armar_num(cadena)
            if token and cadena: 
                n_columna +=1
                #arma el lexema
                n = Num(token, n_linea, n_columna)
                
                lista_lexema.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
                
        elif char == '[' or char == ']':
            #arma el lexema
            c = Lexema(char, n_linea, n_columna)
            
            lista_lexema.append(c)
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
            continue
        
        elif char == '\t':
            n_columna += 4
            cadena = cadena[1:]
            puntero = 0
            continue
                
        elif char == ':':
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
            continue
        
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
            continue
        
        elif char == ' ':
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
            continue
        
        elif char == ',':
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
            continue
        
        elif char == '{':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
            continue
        
        elif char == '}':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
            continue

        else:
            # si no es un caracter reconocido, es un error
            mensaje = f"Error léxico: caracter no reconocido '{char}'"
            e = Error(mensaje, n_linea, n_columna)
            lista_errores.append(e)
            
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            
    for lexema in lista_lexema:
        print(lexema.get_valor())
        
    for error in lista_errores:
        print(f"{error.mensaje} en línea {error.linea}, columna {error.columna}")
        
    return lista_lexema, lista_errores



def armar_Lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexema
    lexema = ''
    puntero = ''
    

    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None

def armar_num(cadena):
    num = '' #token
    puntero = ''
    decimal = False
    
    for char in cadena: 
        puntero += char
        if char == '.':
            decimal = True
        if char == '\"' or char == ' ' or char == '\n' or char == ']' or char == '\t':
            if decimal:
                return float(num), cadena[len(puntero)-1:]
            else:
                return int(num),cadena[len(puntero)-1:]
        else:
            num += char
    return None, None

def operar():
    global lista_lexema
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    
    while lista_lexema:
        lexema = lista_lexema.pop(0)
        if lexema.operar(None) == 'Operacion':
            operacion = lista_lexema.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexema.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexema.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()
            
        
        if operacion and n1 and n2:
            return Aritmetica(n1,n2,operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna}')
        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

def operar_R():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    for instruccion in instrucciones:
        print(instruccion.operar(None))
    return instrucciones


