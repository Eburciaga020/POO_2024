"""
una funcion es un conjunto de intrucciones 
agrupados bajo un nombre en particular como un 
programa mas pequno que cumple una funcion
especifica. La funcion se puede reutilizar con 
el simple hecho de invocarla es decir mandarla
llamar

sintaxis:

def nombredeMifucion(parametros):
bloque o cunjunto de instrucciones

nombredeMifucion(parametros)

Las fuciones pueden ser de 4 tipos
1.Funciones que no recibe parametros y no regresa valor
2.Funciones que no recibe parametros y regresa valor
3.Funciones que recibe parametros y no regresa valor 
4.Funciones que recibe parametros y regresa valor
"""

# 1.Funciones que no recibe parametros y no regresa valor

def sumaNumeros1():
    n1=int(input("Numero #1 : "))
    n2=int(input("Numero #2 : "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

sumaNumeros1()

# 2.Funciones que no recibe parametros y regresa valor 

def sumaNumeros2():
    n1=int(input("Numero #1 : "))
    n2=int(input("Numero #2 : "))
    suma=n1+n2
    return f"{n1}+{n2}={suma}"

print(sumaNumeros2())

# 3.Funciones que recibe parametros y no regresa valor

def sumaNumeros3(n1,n2):
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

n1=int(input("Numero #1 : "))
n2=int(input("Numero #2 : "))

sumaNumeros3(n1,n2)

# 4.Funciones que recibe parametros y regresa valor

def sumaNumeros4(n1,n2):
    suma=n1+n2
    return f"{n1}+{n2}={suma}"

n1=int(input("Numero #1 : "))
n2=int(input("Numero #2 : "))

print(sumaNumeros4(n1,n2))

"""
Ejemplo 6 Crear un programa que solicite a traves de una funcion la siguientes informacion:
Nombre del paciente, Edad, Estatura, Tipo de sangre. Utilizar los 4 tipos de funciones 
"""