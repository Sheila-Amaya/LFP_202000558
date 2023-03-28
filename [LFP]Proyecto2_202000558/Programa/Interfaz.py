from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from analizador import *
from tkinter.filedialog import asksaveasfilename
import os
from analizador import instruccion
import json
from tkinter import messagebox

lista_errores = []

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
        ventana_secundaria.iconbitmap(r'C:\Users\amaya\OneDrive\Documents\GitHub\LFP_202000558\[LFP]Proyecto2_202000558\Programa\pl.ico')
    
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
        opciones_menu.add_command(label="Guardar",command=lambda: self.guardar(cuadro_texto))
        opciones_menu.add_command(label="Guardar como",command=lambda: self.guardar_como(cuadro_texto))
        opciones_menu.add_command(label="Analizar", command=lambda: self.analizar(cuadro_texto.get("1.0", END)))
        opciones_menu.add_command(label="Error", command=lambda: self.escribir_error())
        opciones_menu.add_separator()
        opciones_menu.add_command(label="Regresar", command=lambda: self.mostrar_principal(principal, ventana_secundaria))
    
        # Agregar opciones al menú de archivo
        menubar.add_cascade(label="Archivo", menu=opciones_menu)
    
        # Crear el menú de ayuda
        ayuda_menu = Menu(menubar, tearoff=0)
        ayuda_menu.add_command(label="Manual de usuario", command=lambda: self.manual_usuario())
        ayuda_menu.add_command(label="Manual técnico", command=lambda: self.manual_tecnico())
        ayuda_menu.add_command(label="Temas de ayuda", command=lambda: self.Temas_ayuda(ventana_secundaria)) #se llama al método Temas_ayuda cuando se hace clic
    
        # Agregar el menú de ayuda
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)
    
        # Asignar el menubar ala ventana secundaria
        ventana_secundaria.config(menu=menubar)
        
    
        # Mostrar la ventana secundaria
        ventana_secundaria.mainloop()
        
    def abrir(self, cuadro_texto):
        try:
            filename = askopenfilename(title='Selecciona un archivo') # solo permite archivos JSON 
            with open(filename, encoding='utf-8') as infile:
                contenido = infile.read()
                cuadro_texto.delete(1.0, END) # Limpiar el cuadro de texto (el indice 1.0 indica la posicion del cursor en el Ct al eliminar cont. anterior)
                cuadro_texto.insert(END, contenido) # Insertar el contenido del archivo en el cuadro de texto
                self.ruta_archivo = filename # almacena la ruta del archivo
        
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo no encontrado o no existe")
        except:
            messagebox.showerror("Error", "Error al abrir archivo")
            self.analizar()

    def analizar(self, contenido):
        global lista_errores
        lista_errores =instruccion(contenido)
        operar_R()
        mensaje1 = graficar(contenido)
        
        root = Tk()
        root.withdraw()
        messagebox.showinfo(title="Mensaje", message=mensaje1)

    def escribir_error(self):
        global lista_errores
        if lista_errores:
            errores = []
            i= 0
            for i, error in enumerate(lista_errores):
                for e in error:
                    errores.append({
                        "No.": i,
                        "Descripcion-Token": {
                            "Lexema": e.lexema.strip('\"'),
                            "Tipo": e.tipo,
                            "Columna": e.columna,
                            "Fila": e.linea
                        }
                    })
                    i += 1
            if errores:
                mensaje2 = "Tabla de errores generada correctamente."
                with open(r"C:\Users\amaya\OneDrive\Documents\GitHub\LFP_202000558\[LFP]Proyecto2_202000558\ERRORES\ERRORES_202000558.json", "w") as f:
                    json.dump(errores, f, indent=4)
                    root = Tk()
                    root.withdraw()
                    messagebox.showinfo(title="Mensaje", message=mensaje2)
                    root.mainloop()
            else:
                mensaje1 ="No se encontraron errores."
                root = Tk()
                root.withdraw()
                messagebox.showinfo(title="Mensaje", message=mensaje1)
                root.mainloop()

    def guardar(self, cuadro_texto):
        try:
            if self.ruta_archivo:  # si hay una ruta de archivo almacenada
                with open(self.ruta_archivo, 'w', encoding='utf-8') as outfile:
                    outfile.write(cuadro_texto.get("1.0", END)) # Escribir el contenido del cuadro de texto en el archivo
                    messagebox.showinfo("Archivo guardado", "El archivo se ha guardado correctamente")
            else:
                self.guardar_como(cuadro_texto)  # si no hay una ruta de archivo almacenada, llamar a guardar_como
        except:
            messagebox.showerror("Error", "No se pudo guardar el archivo")

    def guardar_como(self, cuadro_texto):
        try:
            contenido = cuadro_texto.get("1.0", END)  # Obtener el contenido del cuadro de texto
            filename = asksaveasfilename(title='Guardar archivo', defaultextension='.json', 
                                        filetypes=[('JSON files', '*.json')]) # seleccionar la ubicación y nombre del archivo a guardar
            with open(filename, 'w', encoding='utf-8') as outfile:
                outfile.write(contenido) # Escribir el contenido del cuadro de texto en el archivo
                messagebox.showinfo("Guardar", "Archivo guardado correctamente") # Mostrar mensaje de que se guardo
        except:
            messagebox.showerror("Error", "Error al guardar el archivo") # Mostrar mensaje de error
        
        
    def Temas_ayuda(self,Secundaria):
        # Ocultar la ventana secundaria
        Secundaria.withdraw()
        
        # Crear la ventana secundaria
        ventana_ayuda = Toplevel()
        ventana_ayuda.title("Temas de ayuda")
        ventana_ayuda.config(bg="AntiqueWhite") #Color de el backgraund
        ventana_ayuda.iconbitmap(r'C:\Users\amaya\OneDrive\Documents\GitHub\LFP_202000558\[LFP]Proyecto2_202000558\Programa\pl.ico')
    
        # Obtener el ancho y alto de la pantalla
        ancho = ventana_ayuda.winfo_screenwidth() # metodo para obtener el ancho de la pantalla en píxeles
        alto = ventana_ayuda.winfo_screenheight()

        # Obtener el ancho y alto de la ventana
        ancho_ventana = 800
        alto_ventana = 400

        # Calcular la posición x e y para centrar la ventana
        x = (ancho / 2) - (ancho_ventana / 2)
        y = (alto / 2) - (alto_ventana / 2)

        # Establecer la geometría de la ventana
        ventana_ayuda.geometry("%dx%d+%d+%d" % (ancho_ventana, alto_ventana, x, y))
        ventana_ayuda.resizable(0, 0) # para no redimensionar la pantalla
    
        # Agregar contenido a la ventana secundaria
        lbl = Label(ventana_ayuda)
        lbl.pack()
        
        # Crear el botón para regresar a la ventana secundaria
        btn_regresar = Button(ventana_ayuda, text="Regresar", command=lambda: self.mostrar_secundaria(Secundaria, ventana_ayuda))
        btn_regresar.place(x=565, y=330, width=200, height=50)
        
        lbl1 = Label(ventana_ayuda, text="\t   Estudiante:\tSheila Elizabeth Amaya Rodríguez ", font=("Courier New",12))
        lbl1.configure(bg="AntiqueWhite")
        lbl1.place(x=90, y=125)
        
        lbl2 = Label(ventana_ayuda, text="\t   Curso:\tLenguajes formales de programación ", font=("Courier New",12))
        lbl2.configure(bg="AntiqueWhite")
        lbl2.place(x=90, y=150)
        
        lbl3 = Label(ventana_ayuda, text="\t   Seccion:\tB+ ", font=("Courier New",12))
        lbl3.configure(bg="AntiqueWhite")
        lbl3.place(x=90, y=175)
        
        lbl4 = Label(ventana_ayuda, text="\t   Carné:\t202000558 ", font=("Courier New",12))
        lbl4.configure(bg="AntiqueWhite")
        lbl4.place(x=90, y=200)
        
        # Mostrar la ventana de temas de ayuda
        ventana_ayuda.mainloop()
        
        
    def manual_usuario(self):
        os.startfile(r'C:\Users\amaya\OneDrive\Documents\GitHub\LFP_202000558\[LFP]Proyecto2_202000558\Documentacion\MANUAL_USUARIO_LFP.pdf')
    
    def manual_tecnico(self):
        os.startfile(r'C:\Users\amaya\OneDrive\Documents\GitHub\LFP_202000558\[LFP]Proyecto2_202000558\Documentacion\MANUAL_TECNICO_LFP.pdf')
        
    def mostrar_secundaria(self, Secundaria, ventana_tres):
        ventana_tres.destroy() #oculta la ventana de ayuda
        Secundaria.deiconify() #muestra la ventana secundaria
        
    def mostrar_principal(self, principal, ventana_secundaria):
        ventana_secundaria.destroy()
        principal.deiconify() #permite ver una ventana que ha sido cerrada previamente
        

    def principal(self):
        # Creando el objeto ventana
        raiz = Tk()

        # Asignar un título a la ventana
        raiz.title("Principal")
        raiz.iconbitmap(r'C:\Users\amaya\OneDrive\Documents\GitHub\LFP_202000558\[LFP]Proyecto2_202000558\Programa\pl.ico') # Establecer el icono de la ventana
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

        lbl2 = Label(raiz, text="\t   Analizador Lexico ", font=("Courier New",12))
        lbl2.configure(bg="AntiqueWhite")
        lbl2.place(x=100, y=75)
        
        funciones = Funciones()  # instancia de la clase Funciones

        btn1 = Button(raiz, text="Iniciar", command = lambda: Funciones().Secundaria(raiz))
        btn1.place(x=85, y=120, width=200, height=50)

        btn = Button(raiz, text="Salir", command=lambda: Funciones().salir(raiz))
        btn.place(x=300, y=120, width=200, height=50)


        raiz.mainloop() #se corre el ciclo principal de la vantana