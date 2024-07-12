from ConexionBD import *

try:  
 micursor=conexion.cursor()
 sql="insert into clientes (id,nombre,direccion,telefono) values (NULL, 'Juan polainas','Col. del valle', '6181234567')" 

 micursor.execute(sql)
 # Es necesario ejecutra el commit para que finalice el SQL con exito
 conexion.commit()
except:
 print(f"Ocurrio un error por favor vuelva a intentar mas tarde") 
else: 
 print("Se creo la tabla con exito")

