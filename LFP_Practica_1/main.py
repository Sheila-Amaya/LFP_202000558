
import os
from Pelicula import Pelicula
from Lista_enlazada import *
from Lectura import *

lista_pelis = Lista_enlazada() #Lista global de todas las peliculas

def limpiarPantalla():
    os.system('cls') #comando para limpiar la pantalla en windows


def pantallaInicio():
    print("\n============================================================")
    print("*\t  LENGUAJES FORMALES Y DE PROGRAMACIÓN             *")
    print("*\t  Sección: B+                                      *")
    print("*\t  Carné:   202000558                               *") 
    print("*\t  Nombre:  Sheila Elizabeth Amaya Rodríguez        *")
    print("============================================================\n")

    input("PRESS ENTER")
    limpiarPantalla()
    menu()

def menu():
    global lista_pelis
    
    
    while True:
            print()
            print("=======================MENU PRINCIPAL=======================")
            print("\t\t1. Cargar archivo entrada              ")  
            print("\t\t2. Gestionar películas                ")
            print("\t\t3. Filtrado ")
            print("\t\t4. Gráfico ")
            print("\t\t5. Salir ")
            print("============================================================\n")
            opc = input("Ingrese una opcion... ")
            limpiarPantalla()

            if opc == "1":
                while True:
                    nombreArchivo = input("\nIngrese el nombre del archivo de entrada ---» ")
                    ruta="../Archivo/"+nombreArchivo+".lfp"
                    lector = Lectura() #intancia de la clase para leer el archivo
                    nuevas_pelis = lector.cargaArchivo(ruta) #se pasa como argumento la ruta del archivo

                    if nuevas_pelis: #si la lista no esta vacia
                        actual = nuevas_pelis.primero #Se obtiene el primer nodo de la lista
                        while actual: # Recorre la lista de nuevas películas y las agrega una por una a la lista global
                            lista_pelis.insertar(actual.dato)
                            actual = actual.siguiente

                    op= input("Desea cargar otro archivo? 1.si 2.No: ")
                    if op != "1":
                        break
                limpiarPantalla()

            elif opc == "2":
                op = None
                while (op != 3):
                    print("\n=====================GESTIONAR PELICULAS====================")
                    print( "\t\t1.Mostrar peliculas")
                    print( "\t\t2.Mostrar Actores")
                    print( "\t\t3.Regresar a menu principal")
                    print("============================================================\n")
                    o = input("Ingrese una opcion... ")
                    limpiarPantalla()

                    if o == "1":
                        print('\n===================== PELICULAS ==========================')
                        lista_pelis.mostrarPelicula()
                        print("===========================================================\n")

                    elif o == "2":
                        print("\n============================================================")
                        lista_pelis.mostrarActores()
                        print("============================================================\n")
                    elif o == "3":
                        menu()



            elif opc == "3":
                pass
            elif opc == "4":
                if lista_pelis:
                    lista_pelis.mostrar()
                else:
                    print("Primero debe cargar un archivo de entrada.")
            elif opc == "5":
                exit(0)
            else:
                print("Ingrese una opción valida, por favor.")



if __name__ == '__main__':
    pantallaInicio()
