from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from analizador import *

class Funciones():
    
    def salir(self, ventana):
        ventana.destroy() #se utiliza para eliminar un widget 
    
    def Secundaria(self, principal):
        # Ocultar la ventana principal
        principal.withdraw()
    
        # Crear la ventana secundaria
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("Iniciar")
        ventana_secundaria.config(bg="AntiqueWhite") #Color de el backgraund
        ventana_secundaria.iconbitmap(r'C:\Users\amaya\OneDrive\Desktop\[LFP]Proyecto2_202000558\Programa\pl.ico')
    
        # Obtener el ancho y alto de la pantalla
        ancho = ventana_secundaria.winfo_screenwidth() # metodo para obtener el ancho de la pantalla en píxeles
        alto = ventana_secundaria.winfo_screenheight()

        # Obtener el ancho y alto de la ventana
        ancho_ventana = 800
        alto_ventana = 400

        # Calcular la posición x e y para centrar la ventana
        x = (ancho / 2) - (ancho_ventana / 2)
        y = (alto / 2) - (alto_ventana / 2)

        # Establecer la geometría de la ventana
        ventana_secundaria.geometry("%dx%d+%d+%d" % (ancho_ventana, alto_ventana, x, y))
        ventana_secundaria.resizable(0, 0) # para no redimensionar la pantalla
    
        # Agregar contenido a la ventana secundaria
        lbl = Label(ventana_secundaria)
        lbl.pack()
        
        #crear el cuadro de texto
        cuadro_texto = Text(ventana_secundaria, height=20, width=80)
        cuadro_texto.pack()
    
        # Crear el menubar
        menubar = Menu(ventana_secundaria)
    
        # Crear el menú de opciones (barra)
        opciones_menu = Menu(menubar, tearoff=0)
        opciones_menu.add_command(label="Abrir" ,command=lambda: self.abrir(cuadro_texto))
        opciones_menu.add_command(label="Guardar")
        opciones_menu.add_command(label="Guardar como")
        opciones_menu.add_command(label="Analizar")
        opciones_menu.add_command(label="Errores")
        opciones_menu.add_separator()
        opciones_menu.add_command(label="Regresar", command=lambda: self.mostrar_principal(principal, ventana_secundaria))
    
        # Agregar opciones al menú de archivo
        menubar.add_cascade(label="Archivo", menu=opciones_menu)
    
        # Crear el menú de ayuda
        ayuda_menu = Menu(menubar, tearoff=0)
        ayuda_menu.add_command(label="Manual de usuario")
        ayuda_menu.add_command(label="Manual técnico")
        ayuda_menu.add_command(label="Temas de ayuda")
    
        # Agregar el menú de ayuda
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)
    
        # Asignar el menubar a la ventana secundaria
        ventana_secundaria.config(menu=menubar)
        
    
        # Mostrar la ventana secundaria
        ventana_secundaria.mainloop()
        
    def abrir(self, cuadro_texto):
        try:
            filename = askopenfilename(title='Selecciona un archivo', 
                                        filetypes=[('JSON files', '*.json')]) # solo permite archivos JSON 
            with open(filename, encoding='utf-8') as infile:
                contenido = infile.read().strip().replace(" ", "")  # Eliminar espacios en blanco
                cuadro_texto.delete(1.0, END) # Limpiar el cuadro de texto (el indice 1.0 indica la posicion dek cursos en el Ct al eliminar cont. anterior)
                cuadro_texto.insert(END, contenido) # Insertar el contenido del archivo en el cuadro de texto
                instruccion(contenido) # Llamar a la función instruccion con el contenido del archivo como argumento
        except:
            messagebox.showerror("Error", "Archivo incorrecto")
        
    def mostrar_principal(self, principal, ventana_secundaria):
        ventana_secundaria.destroy()
        principal.deiconify() #permite ver una ventana que ha sido cerrada previamente
    

    def principal(self):
        # Creando el objeto ventana
        raiz = Tk()

        # Asignar un título a la ventana
        raiz.title("Principal")
        raiz.iconbitmap(r'C:\Users\amaya\OneDrive\Desktop\[LFP]Proyecto2_202000558\Programa\pl.ico') # Establecer el icono de la ventana
        raiz.config(bg="AntiqueWhite") #Color de el backgraund

        # Obtener el ancho y alto de la pantalla
        ancho = raiz.winfo_screenwidth() #metodo para obtener el ancho de la pantalla en píxeles
        alto = raiz.winfo_screenheight()

        # Obtener el ancho y alto de la ventana
        ancho_ventana = 600
        alto_ventana = 250

        # Calcular la posición x e y para centrar la ventana
        x = (ancho / 2) - (ancho_ventana / 2)
        y = (alto / 2) - (alto_ventana / 2)

        # Establecer la geometría de la ventana
        raiz.geometry("%dx%d+%d+%d" % (ancho_ventana, alto_ventana, x, y))
        raiz.resizable(0,0) #para no redimensionar la pantalla 

        lbl = Label(raiz, text="▬▬▬▬▬▬▬▬▬▬▬▬ Bienvenido ▬▬▬▬▬▬▬▬▬▬▬▬", font=("Courier New",16), padx=24, pady=20)
        lbl.configure(bg="AntiqueWhite")
        lbl.place(x=30, y=20)

        lbl2 = Label(raiz, text=" Lenguajes Formales y de Programación ", font=("Courier New",12))
        lbl2.configure(bg="AntiqueWhite")
        lbl2.place(x=100, y=75)
        
        funciones = Funciones()  # instancia de la clase Funciones

        btn1 = Button(raiz, text="Iniciar", command = lambda: Funciones().Secundaria(raiz))
        btn1.place(x=85, y=120, width=200, height=50)

        btn = Button(raiz, text="Salir", command=lambda: Funciones().salir(raiz))
        btn.place(x=300, y=120, width=200, height=50)


        raiz.mainloop() #se corre el ciclo principal de la vantana