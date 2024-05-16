# Ciclo for estructura interativa que se ejecuta x veces

#sintaxis
#for (Variables) in (elementos_interable) (lista, rango, etc)
    #bloque de interacciones

#Ejemplo 1 crear un programa que imprima 5 veces el @

i=1

for i in range(1,6):
    print("@")

#Ejemplo 2 crear un programa que imprima los numeros del 1 al 5 y los sume y que al final imprima la suma 

contador=1
suma=0

for contador in range(1,6):
    print(contador)
    suma+=contador

print(f"La suma es: {suma}")

#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desea

tabla=int(input("Ingresa un numero para calcular su tabla de multiplicar: ")) 

i=1
multi=0

for i in range(1,11):
    multi=i*tabla
    print(f"{tabla} X {i} = {multi}")