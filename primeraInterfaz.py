from tkinter import*
raiz=Tk() #me permite instanciar la ventana
raiz.title("Primera Ventana")
#raiz.config(width=500, height=500)
raiz.resizable(0,0) #bloquea cambiar tamanio
raiz.iconbitmap("imagen.ico") #coloco un icono en titulo
raiz.config(bg="steel blue") #colocamos fondo azul
raiz.geometry("600x350")
miFrame=Frame() #colocamos un frame
miFrame.pack(fill="both", expand=True) #especifica que esta dentro de la ventana 
miFrame.config(bg="red", width=100, height=100, bd=35, relief="groove") # fondo, tamanio, borde 



raiz.mainloop()
