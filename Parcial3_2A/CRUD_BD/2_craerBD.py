import mysql.connector

try:
 #Conexion con la BD de Mysql
 conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
 
#Crear un objeto nuevo de tipo cursor para ejecutar SQL
 micursor=conexion.cursor()

 sql="create database bd_python"

 micursor.execute(sql) 

except Exception as e:
 print(f"Error: {e}")
 print(f"Tipo de error: {type(e).__name__}")
 print(f"Ocurrio un error por favor vuelva a intentar mas tarde")

else:
 print(f"Se creo la base de datos exitosamente")
 micursor.execute("Show databases")
 for x in micursor:
  print(x)