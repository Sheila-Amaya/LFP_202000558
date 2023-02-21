
import os
from Pelicula import Pelicula
from Lista_enlazada import Lista_enlazada
from Lectura import *


lista_pelis = Lista_enlazada() #Lista global que almacena  todas las peliculas 

def limpiarPantalla():
    os.system('cls') #comando para limpiar la pantalla en windows


def pantallaInicio():
    print("=====================================================================")
    print("*\t  LENGUAJES FORMALES Y DE PROGRAMACIÓN                      *")
    print("*\t  Sección: B+                                               *")
    print("*\t  Carné:   202000558                                        *") 
    print("*\t  Nombre:  Sheila Elizabeth Amaya Rodríguez                 *")
    print("=====================================================================")

    input("PRESS ENTER")
    limpiarPantalla()
    menu()

def menu():
    global lista_pelis
    
    
    while True:
            print()
            print("=========================== MENU PRINCIPAL ============================")
            print("\t\t1. Cargar archivo entrada              ")  
            print("\t\t2. Gestionar películas                ")
            print("\t\t3. Filtrado ")
            print("\t\t4. Gráfico ")
            print("\t\t5. Salir ")
            print("=====================================================================\n")
            opc = input("Ingrese una opcion... ")
            limpiarPantalla()

            if opc == "1":
                while True:
                    print("\n=====================================================================\n")
                    nombreArchivo = input(" Ingrese el nombre del archivo de entrada ---» ").strip()
                    ruta="../Archivo/"+nombreArchivo+".lfp"
                    lector = Lectura() #intancia de la clase para leer el archivo
                    nuevas_pelis = lector.cargaArchivo(ruta) #se pasa como argumento la ruta del archivo
                    print("\n Se cargo el archivo correctamente.")
                    if nuevas_pelis: #si la lista no esta vacia
                        actual = nuevas_pelis.primero #Se obtiene el primer nodo de la lista
                        while actual: # Recorre la lista de nuevas películas y las agrega una por una a la lista global
                            lista_pelis.insertar(actual.dato)
                            actual = actual.siguiente

                    op= input("\nDesea cargar otro archivo? 1.si 2.No: ").strip()
                    print("=====================================================================\n")
                    if op != "1":
                        break
                limpiarPantalla()

            elif opc == "2":
                op = None
                while (op != 3):
                    print("\n======================== GESTIONAR PELICULAS ======================")
                    print( "\t\t1.Mostrar peliculas")
                    print( "\t\t2.Mostrar Actores")
                    print( "\t\t3.Regresar a menu principal")
                    print("=====================================================================\n")
                    o = input("Ingrese una opcion... ")
                    limpiarPantalla()

                    if o == "1":
                            print('\n========================== PELICULAS ==============================')
                            lista_pelis.mostrarPelicula()
                            print("=====================================================================\n")

                    elif o == "2":
                        print("\n============================ ACTORES ==============================")
                        lista_pelis.mostrarActores()
                        print("=====================================================================\n")
                    elif o == "3":
                        menu()



            elif opc == "3":
                op = None
                while (op != 3):
                    print("\n============================== FILTRADO ===========================")
                    print( "\t\t1.Por Actor")
                    print( "\t\t2.Por Año")
                    print( "\t\t3.Por Genero")
                    print( "\t\t4.Regresar")
                    print("=====================================================================\n")
                    o = input("Ingrese una opcion... ").strip()
                    limpiarPantalla()
                    
                    if o == "1":
                        print('\n========================== LISTA DE ACTORES =======================')
                        lista_pelis.mostrarActores()
                        name = input("\nIngrese el nombre del actor para ver las peliculas en las que ha actuado:  ").strip()
                        lista_pelis.buscar_actor(name)
                        print("=====================================================================\n")
                    elif o == "2":
                        print('\n========================== LISTA POR AÑO ==========================')
                        entrada = input("Ingrese el año de la pelicula que desea buscar: ").strip()
                        print()
                        lista_pelis.buscar_anio(entrada)
                        print("=====================================================================\n")
                    elif o == "3":
                        print('\n======================== LISTA POR GENERO =========================')
                        genero = input("Ingrese el genero : ").strip()
                        lista_pelis.buscar_genero(genero)
                        print("=====================================================================\n")
                    elif o == "4":
                        menu()

            elif opc == "4":
                lista_pelis.graph()
            elif opc == "5":
                print("¡Hasta pronto!")
                input("presiona cualquier letra para continuar...")
                limpiarPantalla()
                exit(0)
            else:
                print("Ingrese una opción valida, por favor.")


if __name__ == '__main__':
    pantallaInicio()
