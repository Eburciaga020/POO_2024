#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

if inicio < fin:
    for i in range(inicio + 1, fin):
        print(i)
elif inicio > fin:
    for i in range(fin + 1, inicio):
        print(i)
else:
    print("Los números son iguales, no hay números entre ellos.")