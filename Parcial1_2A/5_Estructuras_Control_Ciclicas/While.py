# Ciclo while estructura interativa que se ejecuta x veces siempre y cuando la condicion se cumla y se seguira ejecutado tanta veces como sea True la condicion

#sintaxis
#while condicion:
    #bloque de intrucciones

#Ejemplo 1 crear un programa que imprima 5 veces el @

contador=1

while contador<=5:
    print("@")
    contador+=1

#Ejemplo 2 crear un programa que imprima los numeros del 1 al 5 y los sume y que al final imprima la suma 

contador=1
suma=0

while contador<=5:
    print(contador)
    suma+=contador
    contador+=1

print(f"La suma es: {suma}")

#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desea

tabla=int(input("Ingresa un numero para calcular su tabla de multiplicar: ")) 

i=1
multi=0

while i<=10:
    multi=i*tabla
    print(f"{tabla} X {i} = {multi}")
    i+=1