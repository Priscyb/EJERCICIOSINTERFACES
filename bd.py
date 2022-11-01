import sqlite3

#Crear una conexion a bd
miConexion=sqlite3.connect("PrimeraBase") #creamos la conexion
#debemos crear un cursor de la conexion
cursor=miConexion.cursor()
#cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(25), CANTIDAD INTEGER, OBSERVACION VARCHAR(45))")
#cursor.execute("INSERT INTO PRODUCTOS VALUES (NULL, 'PC', '5', 'No hay Observacion')")
""""
productos=[
    ('PC', '5', 'No hay Observacion'),
    ('Mouse', '8', 'No hay Observacion'),
    ('Pantalla', '9', 'No hay Observacion'),
    ('Flash', '10', 'No hay Observacion')

]
cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)
"""
cursor.execute("SELECT * FROM PRODUCTOS")
listaProductos=cursor.fetchall()
for producto in listaProductos: #le doy un formato de salida a los datos a mostrar
    print("ID: ",producto[0], "Nombre: ",producto[1], "Cantidad: ", producto[2], "Observacion: ", producto[3])
#print(listaProductos) imprime la lista de productos sin formato
#cursor.execute("UPDATE PRODUCTOS SET CANTIDAD=20 WHERE ID=1")
#cursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")
miConexion.commit()

miConexion.close() #cerramos la conexion

