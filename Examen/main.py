from POO import *
from conexion import *
#listo
def menu():
    conexion = crear_conexion()
    if conexion:
        while True:
            print("\n--- Menú de Opciones ---")
            print("1. Crear Cliente")
            print("2. Culsutar Cliente")
            print("3. Actualizar Cliente")
            print("4. Eliminar Cliente")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                nif = input("Nif: ")
                nombre = input("Nombre: ")
                direccion = input("Direccion: ")
                ciudad = input("Ciudad: ")
                tel = input("Tel: ")
                Empleado.crear_empleado(conexion, nif, nombre, direccion, ciudad, tel)
            elif opcion == '2':
                Empleado.leer_empleados(conexion)
            elif opcion == '3':
                nif = int(input("Nif del clinte que decea actualizar: "))
                nombre = input("Nuevo nombre: ")
                direccion = input("Nuevo Direcccio: ")
                ciudad = input("Nuevo Ciudad: ")
                tel = input("Nuevo Tel: ")
                Empleado.actualizar_empleado(conexion, nif, nombre, direccion, ciudad, tel)
            elif opcion == '4':
                nif = int(input("Nif del clinte a eliminar: ")) 
                Empleado.eliminar_empleado(conexion, id)
            elif opcion == '5':
                cerrar_conexion(conexion)
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()