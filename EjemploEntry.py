from calendar import TextCalendar
from tkinter import*

raiz=Tk()
raiz.title("Formulario")

miNombre=StringVar()#creamos una variable para asignar al textnombre cuando pulse el boton

miFrame=Frame(raiz,width=500,height=500)
miFrame.pack()
raiz.geometry("300x300")

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
    #print("Priscila")
botonEnvio=Button(raiz, text="Enviar", command=codigoBoton) #lo colocamos en la raiz fuera del Frame
botonEnvio.pack()

raiz.mainloop()