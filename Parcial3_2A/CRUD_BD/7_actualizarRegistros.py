from ConexionBD import *

try:  
 micursor=conexion.cursor()
 sql="update clientes set direccion='Col. del Maestro' where id=1" 

 micursor.execute(sql)
 # Es necesario ejecutra el commit para que finalice el SQL con exito
 conexion.commit()
except:
 print(f"Ocurrio un error por favor vuelva a intentar mas tarde") 
else: 
 print("Registro Actualizado con exito")

