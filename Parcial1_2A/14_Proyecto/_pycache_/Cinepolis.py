
def agregar_pelicula(nombre):
    peliculas.append(nombre)
    print(f"Película '{nombre}' agregada.")

def eliminar_pelicula(nombre):
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"Película '{nombre}' removida.")
    else:
        print(f"La película '{nombre}' no se encontró en la lista.")

def actualizar_pelicula(nombre_viejo, nombre_nuevo):
    if nombre_viejo in peliculas:
        index = peliculas.index(nombre_viejo)
        peliculas[index] = nombre_nuevo
        print(f"Película '{nombre_viejo}' actualizada a '{nombre_nuevo}'.")
    else:
        print(f"La película '{nombre_viejo}' no se encontró en la lista.")

def buscar_pelicula(nombre):
    if nombre in peliculas:
        print(f"La película '{nombre}' se encuentra en la lista.")
    else:
        print(f"La película '{nombre}' no se encuentra en la lista.")

def vaciar_lista():
    peliculas.clear()
    print("Todas las películas han sido eliminadas de la lista.")

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
    print("4. Actualizar película")
    print("5. Buscar película")
    print("6. Vaciar lista")
    print("7. Salir")

def menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1" or opcion=="agregar":
            nombre = input("Ingresa el nombre de la película a agregar: ")
            agregar_pelicula(nombre)
        elif opcion == "2" or opcion=="eliminar":
            nombre = input("Ingresa el nombre de la película a eliminar: ")
            eliminar_pelicula(nombre)
        elif opcion == "3" or opcion=="consultar":
            consultar_peliculas()
        elif opcion == "4" or opcion=="actualizar":
            nombre_viejo = input("Ingresa el nombre de la película a actualizar: ")
            nombre_nuevo = input("Ingresa el nuevo nombre de la película: ")
            actualizar_pelicula(nombre_viejo, nombre_nuevo)
        elif opcion == "5" or opcion=="buscar":
            nombre = input("Ingresa el nombre de la película a buscar: ")
            buscar_pelicula(nombre)
        elif opcion == "6" or opcion=="vaciar":
            vaciar_lista()
        elif opcion == "7" or opcion=="salir":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
