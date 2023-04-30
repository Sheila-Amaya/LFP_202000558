from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import os
from tkinter import messagebox
from analizador import *
from tkinter import ttk


class Funciones():
    def __init__(self):
        pass
    
    ruta_icono = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pl.ico")
    
    def salir(self, ventana):
        ventana.destroy() #se utiliza para eliminar un widget 
        ventana.quit() #se utiliza para salir de la aplicación
    
    def Secundaria(self, principal):
        # Ocultar la ventana principal
        principal.withdraw()
    
        # Crear la ventana secundaria
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("Iniciar")
        ventana_secundaria.config(bg="AntiqueWhite") #Color de el backgraund
        ventana_secundaria.iconbitmap(self.ruta_icono)
    
        # Obtener el ancho y alto de la pantalla
        ancho = ventana_secundaria.winfo_screenwidth() # metodo para obtener el ancho de la pantalla en píxeles
        alto = ventana_secundaria.winfo_screenheight()

        # Obtener el ancho y alto de la ventana
        ancho_ventana = 900
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
        cuadro_texto = Text(ventana_secundaria, height=20, width=50)
        cuadro_texto.pack()
        cuadro_texto.place(x=35, y=30) #ubicar el cuadro de texto

        
        #crear el cuadro de texto
        cuadro_texto2 = Text(ventana_secundaria, height=20, width=50)
        cuadro_texto2.pack()
        cuadro_texto2.place(x=460, y=30)#ubicar el cuadro de texto
    
        # Crear el menubar
        menubar = Menu(ventana_secundaria)
    
        # Crear el menú de opciones (barra)
        opciones_menu = Menu(menubar, tearoff=0)
        opciones_menu.add_command(label="Abrir" ,command=lambda: self.abrir(cuadro_texto))
        opciones_menu.add_command(label="Nuevo", command=lambda: self.nuevo(cuadro_texto, cuadro_texto2))
        opciones_menu.add_command(label="Guardar",command=lambda: self.guardar(cuadro_texto))
        opciones_menu.add_command(label="Guardar como",command=lambda: self.guardar_como(cuadro_texto))
        opciones_menu.add_separator()
        opciones_menu.add_command(label="Regresar", command=lambda: self.mostrar_principal(principal, ventana_secundaria))
        # Agregar opciones al menú de archivo
        menubar.add_cascade(label="Archivo", menu=opciones_menu)
    
        # Asignar el menubar ala ventana secundaria
        ventana_secundaria.config(menu=menubar)
        
        # Crear el menú de analisis
        analisis_menu = Menu(menubar, tearoff=0)
        analisis_menu.add_command(label="Generar Sentencias", command=lambda: self.analizar(cuadro_texto.get("1.0", END)))
        menubar.add_cascade(label="Analizar", menu=analisis_menu)
        
        # Crear el menú de token
        token_menu = Menu(menubar, tearoff=0)
        token_menu.add_command(label="Visualizar Tokens", command=lambda: self.ver_token(ventana_secundaria))
        menubar.add_cascade(label="Token", menu=token_menu)
        
        # Crear el menú de errores
        token_menu = Menu(menubar, tearoff=0)
        token_menu.add_command(label="Visualizar Errores", command=lambda: self.ver_Error(ventana_secundaria))
        menubar.add_cascade(label="Error", menu=token_menu)
        
        # Crear el menú de ayuda
        ayuda_menu = Menu(menubar, tearoff=0)
        ayuda_menu.add_command(label="Manual de usuario", command=lambda: self.manual_usuario())
        ayuda_menu.add_command(label="Manual técnico", command=lambda: self.manual_tecnico())
        ayuda_menu.add_command(label="Temas de ayuda", command=lambda: self.Temas_ayuda(ventana_secundaria)) #se llama al método Temas_ayuda cuando se hace clic
    
        # Agregar el menú de ayuda
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)
        
        lbl1 = Label(ventana_secundaria, text="RESULTADO ", font=("Courier New",12))
        lbl1.configure(bg="AntiqueWhite")
        lbl1.place(x=460, y=5)
        
        # Mostrar la ventana secundaria
        ventana_secundaria.mainloop()
        
    def ver_token(self,Secundaria):
        Secundaria.withdraw()
        # Crear la ventana secundaria
        ventana_t = Toplevel()
        ventana_t.title("Tokens encontrados")
        ventana_t.config(bg="AntiqueWhite") #Color de el backgraund
        ventana_t.iconbitmap(self.ruta_icono)
        # Obtener el ancho y alto de la pantalla
        ancho = ventana_t.winfo_screenwidth() # metodo para obtener el ancho de la pantalla en píxeles
        alto = ventana_t.winfo_screenheight()
        # Obtener el ancho y alto de la ventana
        ancho_ventana = 850
        alto_ventana = 600
        # Calcular la posición x e y para centrar la ventana
        x = (ancho / 2) - (ancho_ventana / 2)
        y = (alto / 2) - (alto_ventana / 2)
        # Establecer la geometría de la ventana
        ventana_t.geometry("%dx%d+%d+%d" % (ancho_ventana, alto_ventana, x, y))
        ventana_t.resizable(0, 0) # para no redimensionar la pantalla
        # Agregar contenido
        # Crear el menubar
        menubar = Menu(ventana_t)
        # Crear el menú de archivo
        archivo_menu = Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Regresar", command=lambda: self.mostrar_secundaria(Secundaria, ventana_t))
        # Agregar opciones al menú de archivo
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
        # Asignar el menubar a la ventana
        ventana_t.config(menu=menubar)
        
        # Crear el frame que contendrá la tabla
        tabla_frame = Frame(ventana_t, width=800, height=500)
        tabla_frame.pack(expand=True)

        # Crear la tabla
        tabla = ttk.Treeview(tabla_frame, columns=("Token", "Tipo", "Linea", "Columna"), show="headings")

        # Configurar las columnas
        tabla.heading("Token", text="Token")
        tabla.heading("Tipo", text="Tipo")
        tabla.heading("Linea", text="Linea")
        tabla.heading("Columna", text="Columna")

        # Agregar los datos a la tabla
        analizador = AnalizadorLexico()
        tokens = analizador.tokens

        # Obtener la cantidad de elementos en la lista de tokens
        num_tokens = len(tokens)

        # Verificar si la lista está vacía
        if num_tokens == 0:
            # Si la lista está vacía, borrar los elementos actuales de la tabla
            tabla.delete(*tabla.get_children())
            tabla.update() # Agregar esta línea para actualizar la tabla
        else:
            tabla.delete(*tabla.get_children())
            tabla.update()
            # Si la lista no está vacía, insertar los nuevos elementos en la tabla
            for token in tokens:
                tabla.insert("", "end", values=(token.buffer, token.tipo, token.linea, token.columna))

                # Actualizar la tabla
                tabla.update()
    
        # Crear un scrollbar y vincularlo a la tabla
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Mostrar la tabla en el frame
        tabla.pack(expand=True, fill="both")
        tabla_frame.pack_propagate(0) # Evita que el frame se ajuste al tamaño de su contenido
        tabla_frame.place(x=20, y=20)

        # Mostrar la ventana de gestión de tokens
        ventana_t.mainloop()
        
    #limpiar los cuadros de texto
    def nuevo(self, cuadro_texto1, cuadro_texto2):
        # limpiar cuadros de texto
        cuadro_texto1.delete('1.0', END)
        cuadro_texto2.delete('1.0', END)
        self.limpiartabla()
        
    def limpiartabla(self):
        analizador = AnalizadorLexico()
        analizador.limpiarLista()
        return True

    def ver_Error(self,Secundaria):
        Secundaria.withdraw()
        # Crear la ventana secundaria
        ventana_e = Toplevel()
        ventana_e.title("Errores encontrados")
        ventana_e.config(bg="AntiqueWhite") #Color de el backgraund
        ventana_e.iconbitmap(self.ruta_icono)
        # Obtener el ancho y alto de la pantalla
        ancho = ventana_e.winfo_screenwidth() # metodo para obtener el ancho de la pantalla en píxeles
        alto = ventana_e.winfo_screenheight()
        # Obtener el ancho y alto de la ventana
        ancho_ventana = 850
        alto_ventana = 600
        # Calcular la posición x e y para centrar la ventana
        x = (ancho / 2) - (ancho_ventana / 2)
        y = (alto / 2) - (alto_ventana / 2)
        # Establecer la geometría de la ventana
        ventana_e.geometry("%dx%d+%d+%d" % (ancho_ventana, alto_ventana, x, y))
        ventana_e.resizable(0, 0) # para no redimensionar la pantalla
        # Agregar contenido
        # Crear el menubar
        menubar = Menu(ventana_e)
        # Crear el menú de archivo
        archivo_menu = Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Regresar", command=lambda: self.mostrar_secundaria(Secundaria, ventana_e))
        # Agregar opciones al menú de archivo
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
        # Asignar el menubar a la ventana
        ventana_e.config(menu=menubar)
        
        # Crear el frame que contendrá la tabla
        tabla_frame = Frame(ventana_e)
        tabla_frame.pack(expand=True)
        
        #######################
        # Crear el frame que contendrá la tabla
        tabla_frame = Frame(ventana_e, width=800, height=500)
        tabla_frame.pack(expand=True)

        # Crear la tabla
        tabla = ttk.Treeview(tabla_frame, columns=("Token","Tipo", "Linea", "Columna"), show="headings")

        # Configurar las columnas
        tabla.heading("Token", text="Token")
        tabla.heading("Tipo", text="Tipo")
        tabla.heading("Linea", text="Linea")
        tabla.heading("Columna", text="Columna")

        # Agregar los datos a la tabla
        analizador = AnalizadorLexico()
        errores = analizador.errores
        
        # Obtener la cantidad de elementos en la lista de tokens
        num_e = len(errores)

        # Verificar si la lista está vacía
        if num_e == 0:
            # Si la lista está vacía, borrar los elementos actuales de la tabla
            tabla.delete(*tabla.get_children())
            tabla.update() # Agregar esta línea para actualizar la tabla
        else:
            tabla.delete(*tabla.get_children())
            tabla.update()
            # Si la lista no está vacía, insertar los nuevos elementos en la tabla
            for error in errores:
                tabla.insert("", "end", values=(error.caracter,error.tipo, error.linea, error.columna))

                # Actualizar la tabla
                tabla.update()

        # Mostrar la tabla en el frame
        tabla.pack(expand=True, fill="both")
        tabla_frame.pack_propagate(0) # Evita que el frame se ajuste al tamaño de su contenido
        tabla_frame.place(x=20, y=20)
        ###############

        # Mostrar la ventana de gestión de tokens
        ventana_e.mainloop()
        

    def abrir(self, cuadro_texto):
        try:
            filename = askopenfilename(title='Selecciona un archivo') # Mostrar la ventana de abrir archivos
            with open(filename, encoding='utf-8') as infile: 
                contenido = infile.read()
                cuadro_texto.delete(1.0, END) # Limpiar el cuadro de texto (el indice 1.0 indica la posicion del cursor en el Ct al eliminar cont. anterior)
                cuadro_texto.insert(END, contenido) # Insertar el contenido del archivo en el cuadro de texto
                self.ruta_archivo = filename # almacena la ruta del archivo
        
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo no encontrado o no existe")
        except:
            messagebox.showerror("Error", "Error al abrir archivo")
            self.analizar(contenido)


    def analizar(self, contenido):
        lexico = AnalizadorLexico()
        lexico.analizar(contenido)


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
            filename = asksaveasfilename(title='Guardar archivo', defaultextension='.txt', 
                                        filetypes=[('txt files', '*.txt')]) # seleccionar la ubicación y nombre del archivo a guardar
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
        ventana_ayuda.iconbitmap(self.ruta_icono)
    
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
        os.startfile(r'C:\Users\amaya\OneDrive\Documents\GitHub\LFP_202000558\[LFP]Proyecto2_202000558\Documentacion\MANUAL_USUARIO_LFP.md')
    
    def manual_tecnico(self):
        os.startfile(r'C:\Users\amaya\OneDrive\Documents\GitHub\LFP_202000558\[LFP]Proyecto2_202000558\Documentacion\MANUAL_TECNICO_LFP.md')
        
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
        raiz.iconbitmap(self.ruta_icono) # Establecer el icono de la ventana
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

        lbl2 = Label(raiz, text="\t     Analizador  ", font=("Courier New",12))
        lbl2.configure(bg="AntiqueWhite")
        lbl2.place(x=100, y=75)
        
        funciones = Funciones()  # instancia de la clase Funciones

        btn1 = Button(raiz, text="Iniciar", command = lambda: Funciones().Secundaria(raiz))
        btn1.place(x=85, y=120, width=200, height=50)

        btn = Button(raiz, text="Salir", command=lambda: Funciones().salir(raiz))
        btn.place(x=300, y=120, width=200, height=50)


        raiz.mainloop() #se corre el ciclo principal de la vantana