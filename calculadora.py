from tkinter import *
from math import *
root=Tk()
nombre = StringVar()
texto1=Entry(root,textvariable=nombre)
#texto1.grid(row=0,column=1,pady=5)
texto1.config(fg="red")
texto1.pack()
miFrame = Frame(root,height=500,width=500)
miFrame.pack()
# Create button for next text.
b1 = Button(miFrame, text = " 7 ",command=lambda:text(7))
b1.grid(row=1,column=1,pady=2,padx=2)
b2 = Button(miFrame, text = " 4 ",command=lambda:text(4))
b2.grid(row=2,column=1,pady=2,padx=2)
b3 = Button(miFrame, text = " 1 ",command=lambda:text(1))
b3.grid(row=3,column=1,pady=2,padx=2)
b4 = Button(miFrame, text = " 0 ",command=lambda:text(0))
b4.grid(row=4,column=1,pady=2,padx=2)
#segunda columna
b5 = Button(miFrame, text = " 8 ",command=lambda:text(8))
b5.grid(row=1,column=2,pady=2,padx=2)
b6 = Button(miFrame, text = " 5 ",command=lambda:text(5))
b6.grid(row=2,column=2,pady=2,padx=2)
b7 = Button(miFrame, text = " 2 ",command=lambda:text(2))
b7.grid(row=3,column=2,pady=2,padx=2)
b8 = Button(miFrame, text = " ,  ",command=lambda:text(","))
b8.grid(row=4,column=2,pady=2,padx=2)
#tercera columna
b9 = Button(miFrame, text = " 9 ",command=lambda:text(9))
b9.grid(row=1,column=3,pady=2,padx=2)
b10 = Button(miFrame, text = " 6 ",command=lambda:text(6))
b10.grid(row=2,column=3,pady=2,padx=2)
b11 = Button(miFrame, text = " 3 ",command=lambda:text(3))
b11.grid(row=3,column=3,pady=2,padx=2)

#tercera columna
b13 = Button(miFrame, text = " / ",command=lambda:text("/"))
b13.grid(row=1,column=4,pady=2,padx=2)
b14 = Button(miFrame, text = " * ",command=lambda:text("*"))
b14.grid(row=2,column=4,pady=2,padx=2)
b15 = Button(miFrame, text = " - ",command=lambda:text("-"))
b15.grid(row=3,column=4,pady=2,padx=2)
b16 = Button(miFrame, text = " + ",command=lambda:text("+"))
b16.grid(row=4,column=4,pady=2,padx=2)
# Create button for next text.
valor=""
def  text(X):
    global valor
    valor=valor+str(X)
    nombre.set(valor)


def resultado():
    global valor
    print(valor)
    try:
        opera=str(eval(valor))
        nombre.set(opera)
    except:
        nombre.set("ERROR")
    valor = ""
b12 = Button(miFrame, text = " = ",command=resultado)
b12.grid(row=4,column=3,pady=2,padx=2)
root.mainloop()