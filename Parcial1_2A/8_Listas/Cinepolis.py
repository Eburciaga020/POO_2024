
def agregar_pelicula(nombre):
    peliculas.append(nombre)
    print(f"Película '{nombre}' agregada.")

def eliminar_pelicula(nombre):
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"Película '{nombre}' removida.")
    else:
        print(f"La película '{nombre}' no se encontró en la lista.")

def consultar_peliculas():
    if peliculas:
        print("Películas en la lista:")
        for pelicula in peliculas:
            print(f"- {pelicula}")
    else:
        print("No hay películas en la lista.")


peliculas = []

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar película")
    print("2. Eliminar película")
    print("3. Consultar películas")
    print("4. Salir")

def menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1" or opcion=="AGREGAR":
            nombre = input("Ingresa el nombre de la película a agregar: ")
            agregar_pelicula(nombre)
        elif opcion == "2" or opcion=="ELIMINAR":
            nombre = input("Ingresa el nombre de la película a eliminar: ")
            eliminar_pelicula(nombre)
        elif opcion == "3":
            consultar_peliculas()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()