
numeros = [8, 3, 1, 7, 4, 6, 2, 5]

print("Lista original:")
for numero in numeros:
    print(numero)

def lista_a_string(lista):
    return ', '.join(map(str, lista))

resultado_string = lista_a_string(numeros)
print("\nLista como string:")
print(resultado_string)

numeros_ordenados = sorted(numeros)
print("\nLista ordenada:")
for numero in numeros_ordenados:
    print(numero)

longitud = len(numeros)
print("\nLongitud de la lista:")
print(longitud)

elemento_buscado = int(input("\nIngrese un número para buscar en la lista: "))
if elemento_buscado in numeros:
    print(f"El número {elemento_buscado} se encuentra en la lista.")
else:
    print(f"El número {elemento_buscado} no se encuentra en la lista.")