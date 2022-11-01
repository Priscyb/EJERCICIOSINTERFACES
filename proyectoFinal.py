from calendar import TextCalendar
from tkinter import*
from tkinter import messagebox
from tkinter.font import BOLD
import sqlite3
from xml.etree.ElementTree import Comment

#creacion de la raiz
raiz=Tk()
raiz.title("Mantenimiento de Persona")

def conectar():
	try:
		miConexion=sqlite3.connect("BaseProyecto")
		cursor=miConexion.cursor()
		messagebox.showinfo("INFORMACION","Conectado correctamente")
		#cursor.execute("CREATE TABLE PERSONAS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_USUARIO VARCHAR(30), APELLIDO VARCHAR(30), PASSWORD VARCHAR(20), DIRECCION VARCHAR(50), COMENTARIOS VARCHAR(100))")
		#miConexion.commit()
		#miConexion.close() #cerramos la conexion
	except:
		messagebox.showwarning("ADVERTENCIA","No se ha podido conectar")
#funciones de los menus
def limpiarCampos():
	#miId.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPassword.set("")
    miComentario.set("")
    Coment.delete(0.0, END)

def infoAdicional():
    messagebox.showinfo("Informacion","Version de codigo 1.0...") #muestra informacion (titulo, contenido)

def acercaDe():
    messagebox.showinfo("Informacion","Realizado por Priscila Bernal")

def insertar():
	miConexion=sqlite3.connect("BaseProyecto")
	cursor=miConexion.cursor()
	try:
		datos=miNombre.get(),miApellido.get(),miPassword.get(),miDireccion.get(),Coment.get("1.0","end-1c")
		cursor.execute("INSERT INTO PERSONAS VALUES(NULL,?,?,?,?,?)", (datos))
		miConexion.commit()
		messagebox.showinfo("Informacion","Registro insertado exitosamente")
		miConexion.close()    
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al insertar el registro")
		pass
	limpiarCampos()

def visualizar():
	miConexion=sqlite3.connect("BaseProyecto")
	cursor=miConexion.cursor()
	try:
		cursor.execute("SELECT * FROM PERSONAS WHERE ID='" +miId.get()+"'")
		ListaPersona=cursor.fetchall()
		for persona in ListaPersona:
			miId.set(persona[0])
			miNombre.set(persona[1])
			miApellido.set(persona[2])
			miPassword.set(persona[3])
			miDireccion.set(persona[4])
			Coment.insert(0.0, persona[5])
	except:
		messagebox.showwarning("ADVERTENCIA","Error al visualizar")
	miConexion.commit()
	miConexion.close()

def actualizar():
	miConexion=sqlite3.connect("BaseProyecto")
	cursor=miConexion.cursor()
	try:
		datos=miNombre.get(),miApellido.get(),miPassword.get(),miDireccion.get(),Coment.get("1.0","end-1c")
		cursor.execute("UPDATE PERSONAS SET NOMBRE_USUARIO=?, APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=? WHERE ID='" +miId.get()+"'",(datos))
		miConexion.commit()
		messagebox.showinfo("Informacion","Registro actualizado exitosamente")
		miConexion.close() 
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
		pass
	limpiarCampos()	

def eliminar():
	miConexion=sqlite3.connect("BaseProyecto")
	cursor=miConexion.cursor()
	try:
		cursor.execute("DELETE FROM PERSONAS WHERE ID='" +miId.get()+"'")
		miConexion.commit()
		messagebox.showinfo("Informacion","Registro eliminado exitosamente")
		miConexion.close() 
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
		pass
	limpiarCampos()			

def salir():
	valor=messagebox.askquestion("Salir","¿Está seguro que desea salir?")
	if valor=="yes":
		raiz.destroy()
		
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
menubd.add_command(label="Conectar", command=conectar)
menubd.add_command(label="Salir", command=salir)
#opciones Borrar
menuBorrar.add_command(label="Borrar campos", command= limpiarCampos)
#opciones del crud
menuCrud.add_command(label="Crear", command=insertar)
#messagebox.showinfo("INFORMACION","Registro insertado correctamente!")
menuCrud.add_command(label="Leer", command=visualizar)
menuCrud.add_command(label="Actualizar", command=actualizar)
menuCrud.add_command(label="Eliminar", command=eliminar)
#opciones de ayuda
menuAyuda.add_command(label="Licencia",command= infoAdicional)#inforAdicional es la funcion creada
menuAyuda.add_command(label="Acerca de...",command= acercaDe)
#LABEL TITULO
labelTitulo=Label(raiz,text="Sistema de Administracion de Personas")
labelTitulo.pack()
labelTitulo.config(fg="blue",font=("Century Gothic",12,BOLD))
#creamos unas variables para asignar a los entry
miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPassword=StringVar()
miDireccion=StringVar()
miComentario=StringVar()
miFrame=Frame(raiz,width=600,height=600)
miFrame.pack()
raiz.geometry("400x350")
#CREACION DE LABELS
labelID=Label(miFrame,text="ID: ",font=("Century Gothic",10))
labelID.grid(row=0,column=0, pady=5)
labelNombre=Label(miFrame,text="Nombre: ",font=("Century Gothic",10))
labelNombre.grid(row=1,column=0, pady=5)
labelApellido=Label(miFrame,text="Apellido: ",font=("Century Gothic",10))
labelApellido.grid(row=2,column=0, pady=5)
labelDireccion=Label(miFrame,text="Direccion: ",font=("Century Gothic",10))
labelDireccion.grid(row=3,column=0, pady=5)
labelPass=Label(miFrame,text="Password: ",font=("Century Gothic",10))
labelPass.grid(row=4,column=0, pady=5)
labelComent=Label(miFrame,text="Comentario: ",font=("Century Gothic",10))
labelComent.grid(row=5,column=0, pady=5)
#CREACION DE ENTRYS
Id=Entry(miFrame, textvariable=miId)
Id.grid(row=0,column=1, pady=5)
Nombre=Entry(miFrame, textvariable=miNombre)
Nombre.grid(row=1,column=1, pady=5)
Apellido=Entry(miFrame, textvariable=miApellido)
Apellido.grid(row=2,column=1, pady=5)
Direccion=Entry(miFrame, textvariable=miDireccion)
Direccion.grid(row=3,column=1, pady=5)
Pass=Entry(miFrame, textvariable=miPassword)
Pass.grid(row=4,column=1, pady=5)
Pass.config(show="*") #para q muestre asteriscos
#comentario es TextArea
Coment=Text(miFrame,width=15,height=5)
Coment.grid(row=5,column=1, pady=5)
#Creamos otro Frame para los botones    
Frame2=Frame()
Frame2=Frame(raiz, width=120,height=600)
Frame2.pack()
botonCrear=Button(Frame2, text="Crear", command=insertar) #lo colocamos en la raiz fuera del Frame
botonCrear.grid(row=0,column=0,padx=5,pady=5)

botonLeer=Button(Frame2, text="Leer", command=visualizar) #lo colocamos en la raiz fuera del Frame
botonLeer.grid(row=0,column=1,padx=5,pady=5)

botonActualizar=Button(Frame2, text="Actualizar", command=actualizar) #lo colocamos en la raiz fuera del Frame
botonActualizar.grid(row=0,column=2,padx=5,pady=5)

botonEliminar=Button(Frame2, text="Eliminar", command=eliminar) #lo colocamos en la raiz fuera del Frame
botonEliminar.grid(row=0,column=3,padx=5,pady=5)

raiz.mainloop()