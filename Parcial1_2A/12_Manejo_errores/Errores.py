"""
Manejo de errores es la forma en la que tiene los lenguajes de programacion
para evitar que sucedan errores en tiempo de ejecucion
"""

#Ejemplo 1 Error cuando una variable no se genera 

# try:
#  nombre=input("Dame el nombre: ")

#  if len(nombre)>1:
#     nombre_usuario="El nombre es: "+nombre

#  print(nombre_usuario)
# except:
#  print("Es necesario introducir un nombre de usurio...")

#Ejemplo cuando se solicita un numero y se introduce una letra 

try:
 numero=(input("Dame un numero: "))

 if numero>0:
  print("Soy numero entero positivo")
 else:
  print("Soy un numero entero negativo")
except:
  print("No se puede convertir un caracter no numerico a numero")
else:
 print("Todo se ejecuto sin errores")

#Ejemplo 3 cuando se generan multiples excepciones
try:
 numero=(int("Dame un numero: "))

 print("El cuadrado es: "+str(numero*numero))
except ValueError:
 print("Debes de introducir un numero no se puede convertir un caracter que no sea numerico")
except TypeError:
 print("No se posible convertir el numero a entero")
else:
 print("Finalizo correctamente")
finally:
 print()