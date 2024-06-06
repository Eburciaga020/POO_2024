"""
List (Array)
Son colleciones o cinjuto de datos/valores bajo
un mismo nombre, para acceder a los valores se
hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y midificable. Permite miembros
duplicados

"""

# Ejemplo 1 Crea un lista con valores numericos enteros e imprimir la lista 

numeros=[23,34]
print(numeros)

#Recorrer la lista con un for

for i in numeros:
    print(i)

#Recorrer la lista con un while

i=0
while i<len(numeros):
    print(numeros[i])
    i+=1

"""
Ejemplo 2 Crea una lista de palabas, posteriormente ingresar una palabra 
para buscar la coincidencia en lista E indicar si aparece la palabra y en que
posicion en caso contrario indicar una sola vez si no lo encuentra
"""

palabras=["hola","2024","10.23","True"]

palabras_buscar=input("Ingresa la palabra a buscar: ")

noencontro=True

# for i in palabras:
#     if palabras_buscar==i:
        # print(f"Encontre la palabra {palabras_buscar}, en la posicion: {palabras.index(i)}")
        # noencontro=False

while i<len(palabras):
   if palabras_buscar==palabras[i]:
      print(f"Encontre la palabra {palabras_buscar}, en la posicion: {palabras.index(i)}")
      noencontro=False



if noencontro:
 print(f"No se encontro la palabra dentro de la lista")