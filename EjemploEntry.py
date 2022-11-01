from calendar import TextCalendar
from tkinter import*
from tkinter import messagebox
from tkinter.font import BOLD

#creacion de la raiz
raiz=Tk()
raiz.title("Mantenimiento de Persona")
#ventanas emergentes
def infoAdicional():
    messagebox.showinfo("Informacion","Version de codigo 1.0...") #muestra informacion (titulo, contenido)
    #messagebox.showwarning("Advertencia","Licencia Caducada") #muestra Advertencias
    #messagebox.showerror("Error","No se puede conectar") #muestra Errores
    #valor=messagebox.askquestion("Atencion","Desea eliminar persona")#ventana de confirmacion
    #print(valor)
    #valor=messagebox.askokcancel("Atencion","Desea salir de la aplicacion")#muestra Ok o Cancelar
    #print(valor)
def acercaDe():
    messagebox.showinfo("Informacion","Realizado por Priscila Bernal")
#CREACION DEL MENU
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)
###oipciones de menu
menubd=Menu(barraMenu, tearoff=0) #tearoff elimina lineas debajo del menu
menuBorrar=Menu(barraMenu, tearoff=0)
menuCrud=Menu(barraMenu, tearoff=0)
menuAyuda=Menu(barraMenu, tearoff=0)
#colocamos la etiquetas de las opciones o submenus
barraMenu.add_cascade(label="BBDD",menu=menubd)
barraMenu.add_cascade(label="Borrar",menu=menuBorrar)
barraMenu.add_cascade(label="CRUD",menu=menuCrud)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
#vamos a agregar los submenus
menubd.add_command(label="Conectar")
menubd.add_command(label="Salir")
#opciones Borrar
menuBorrar.add_command(label="Borrar campos")
#opciones del crud
menuCrud.add_command(label="Crear")
menuCrud.add_command(label="Leer")
menuCrud.add_command(label="Actualizar")
menuCrud.add_command(label="Eliminar")
#opciones de ayuda
menuAyuda.add_command(label="Licencia",command= infoAdicional)#inforAdicional es la funcion creada
menuAyuda.add_command(label="Acerca de...",command= acercaDe)
#LABEL TITULO
labelTitulo=Label(raiz,text="Sistema de Administracion de Personas")
labelTitulo.pack()
labelTitulo.config(fg="blue",font=("Century Gothic",12,BOLD))
miNombre=StringVar()#creamos una variable para asignar al textnombre cuando pulse el boton
miFrame=Frame(raiz,width=600,height=600)
miFrame.pack()
raiz.geometry("400x350")

labelNombre=Label(miFrame,text="Nombre: ",font=("Century Gothic",10))
labelNombre.grid(row=0,column=0, pady=5)
labelApellido=Label(miFrame,text="Apellido: ",font=("Century Gothic",10))
labelApellido.grid(row=1,column=0, pady=5)
labelDireccion=Label(miFrame,text="Direccion: ",font=("Century Gothic",10))
labelDireccion.grid(row=2,column=0, pady=5)
labelPass=Label(miFrame,text="Password: ",font=("Century Gothic",10))
labelPass.grid(row=3,column=0, pady=5)
labelComent=Label(miFrame,text="Comentario: ",font=("Century Gothic",10))
labelComent.grid(row=4,column=0, pady=5)

textNombre=Entry(miFrame, textvariable=miNombre)
textNombre.grid(row=0,column=1, pady=5)
textApellido=Entry(miFrame)
textApellido.grid(row=1,column=1, pady=5)
textDireccion=Entry(miFrame)
textDireccion.grid(row=2,column=1, pady=5)
textPass=Entry(miFrame)
textPass.grid(row=3,column=1, pady=5)
textPass.config(show="*") #para q muestre asteriscos
#comentario es TextArea
textComent=Text(miFrame,width=15,height=5)
textComent.grid(row=4,column=1, pady=5)
#creamos el boton
def codigoBoton (): #creamos la funcion que se envia en el command del boton
    miNombre.set("Priscila")
    
Frame2=Frame()
Frame2=Frame(raiz, width=120,height=600)
Frame2.pack()
botonCrear=Button(Frame2, text="Crear", command=codigoBoton) #lo colocamos en la raiz fuera del Frame
botonCrear.grid(row=0,column=0,padx=5,pady=5)

botonLeer=Button(Frame2, text="Leer", command=codigoBoton) #lo colocamos en la raiz fuera del Frame
botonLeer.grid(row=0,column=1,padx=5,pady=5)

botonActualizar=Button(Frame2, text="Actualizar", command=codigoBoton) #lo colocamos en la raiz fuera del Frame
botonActualizar.grid(row=0,column=2,padx=5,pady=5)

botonEliminar=Button(Frame2, text="Eliminar", command=codigoBoton) #lo colocamos en la raiz fuera del Frame
botonEliminar.grid(row=0,column=3,padx=5,pady=5)

raiz.mainloop()