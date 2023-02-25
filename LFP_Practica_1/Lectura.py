from Lista_enlazada import *
from Pelicula import *

class Lectura:

    def  cargaArchivo(self,ruta):
        try: #manejar excepciones
            with open(ruta, mode="r",encoding='utf-8') as Archivo: #abre el archivo modo lectura
                lista_datos = Archivo.readlines() #lee todas las líneas del archivo y las almacena en la variable 
                return self.procesar_Archivo(lista_datos) #procesar las líneas del archivo leído y retornar una Lista_enlazada de películas.

        #print(Archivo.readlines())
        except FileNotFoundError:
            print("No se pudo encontrar el archivo Por favor, comprueba que el nombre y la ubicación son correctos.")
        except Exception as e:
            print("Ha ocurrido un error al cargar el archivo.")
        finally:
            if Archivo: #cierre automáticamente al finalizar la lectura
                Archivo.close()


    def procesar_Archivo(self,lista_datos):#recibe la lista que contiene las lineas del archivo que se cargo antes
        pelis = Lista_enlazada()
    
        for linea in lista_datos: #procesa cada linea del archivo
            lista_general = linea.strip().split(";") #se divide cada linea utilizando ; de separador
        
            nombre = lista_general[0] #se extrae el nombre
            actor= [a.strip() for a in lista_general[1].split(",")] # se extraen como una cadena separada por , y se convierte a una []
            anio = lista_general[2].strip()
            genero=lista_general[3].strip() #rstrip elimina cualquier espacio en blanco al final de la linea
        
            nueva_peli = Pelicula(nombre,actor,anio,genero) #se almacenan los valores 
            #nuevo = Nodo(nueva_peli)
            #print( "|",(vars(nuevo.dato)))
        
            pelis.insertar(nueva_peli) #se inserta a la lista enlazada
        
        return pelis