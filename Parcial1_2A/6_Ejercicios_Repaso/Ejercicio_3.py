# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

print("Usando while:")
numero = 1
while numero <= 60:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es: {cuadrado}")
    numero += 1

print("\nUsando for:")
for numero in range(1, 61):
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es: {cuadrado}")