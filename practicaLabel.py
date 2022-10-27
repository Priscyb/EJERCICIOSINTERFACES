from tkinter import*
raiz=Tk() #me permite instanciar la ventana

miFrame=Frame(raiz,width=500,height=400) #colocamos un frame
miFrame.pack() #especifica que esta dentro de la ventana 
miLabel=Label(miFrame,text="Hola alumnos python")
#miLabel.pack()
miLabel.place(x=100,y=200)
#Agregamos una imagen
miImagen=PhotoImage(file="imagen.png")
miLabel2=Label(miFrame,image=miImagen)
miLabel2.place(x=100,y=5)
#Cuadros de texto
cuadro1=Entry(miFrame)
cuadro1.place(x=100,y=250)
cuadro1.config(fg="blue",justify="center") #color de letra y centrada
raiz.mainloop()
