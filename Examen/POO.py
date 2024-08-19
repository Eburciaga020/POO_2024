from conexion import *

class Empleado:
    def __init__(self, nif, nombre, direccion, ciudad, tel ):
        self.nif = nif 
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def crear_empleado(conexion, nif, nombre, direccion, ciudad, tel):
        cursor = conexion.cursor()
        query = "INSERT INTO Clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)"
        valores = (nif, nombre, direccion, ciudad, tel)
        cursor.execute(query, valores)
        conexion.commit()
        print("Cliente creado exitosamente")
    
    def leer_empleados(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM Clintes"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"nif: {fila[0]}, Nombre: {fila[1]}, direccion: {fila[2]}, ciudad: {fila[3]},  tel: {fila[4]} ")
            
    def actualizar_empleado(conexion, nif, nombre, direccion, ciudad, tel):
        cursor = conexion.cursor()
        query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE EmpleadoID = %s"
        valores = (nif, nombre, direccion, ciudad, tel)
        cursor.execute(query, valores)
        conexion.commit()
        print("Clintes actualizado exitosamente")

    def eliminar_empleado(conexion, id):
        cursor = conexion.cursor()
        query = "DELETE FROM Clintes WHERE nif = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        print("Clinte eliminado exitosamente")
