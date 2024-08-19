import mysql.connector
import hashlib

# Conexión a la base de datos
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",         # Reemplaza con tu usuario
        password="tu_contraseña",  # Reemplaza con tu contraseña
        database="agencia_autos_datos"
    )

# Función para hashear contraseñas
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Registrar un nuevo usuario
def register_user(username, password):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
    hashed_password = hash_password(password)
    values = (username, hashed_password)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    print("Usuario registrado exitosamente.")

# Autenticar usuario
def login_user(username, password):
    db = connect()
    cursor = db.cursor()
    hashed_password = hash_password(password)
    sql = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, hashed_password))
    result = cursor.fetchone()
    db.close()
    return result is not None

# Menú de registro e inicio de sesión
def login_menu():
    while True:
        print("\nMenú de Usuario")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            register_user(username, password)

        elif opcion == "2":
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            if login_user(username, password):
                print("Inicio de sesión exitoso.")
                return True
            else:
                print("Credenciales incorrectas, intenta de nuevo.")

        elif opcion == "3":
            print("Saliendo del programa...")
            return False

        else:
            print("Opción no válida, intenta de nuevo.")

# Menú interactivo de la agencia de autos
def menu():
    while True:
        print("\nMenú de la Agencia de Autos")
        print("1. Insertar Cliente")
        print("2. Insertar Auto")
        print("3. Insertar Revisión")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nif = int(input("NIF del cliente: "))
            nombre = input("Nombre del cliente: ")
            direccion = input("Dirección del cliente: ")
            ciudad = input("Ciudad del cliente: ")
            tel = int(input("Teléfono del cliente: "))
            insert_cliente(nif, nombre, direccion, ciudad, tel)
            print("Cliente insertado exitosamente.")

        elif opcion == "2":
            matricula = input("Matrícula del auto: ")
            marca = input("Marca del auto: ")
            modelo = int(input("Modelo del auto (Año): "))
            color = input("Color del auto: ")
            nif = int(input("NIF del cliente dueño del auto: "))
            insert_auto(matricula, marca, modelo, color, nif)
            print("Auto insertado exitosamente.")

        elif opcion == "3":
            no_revision = int(input("Número de revisión: "))
            cambiofiltro = input("Cambio de filtro (Y/N): ")
            cambioaceite = input("Cambio de aceite (Y/N): ")
            cambiodiscos = input("Cambio de discos (Y/N): ")
            otros = input("Otros cambios: ")
            matricula = input("Matrícula del auto: ")
            insert_revision(no_revision, cambiofiltro, cambioaceite, cambiodiscos, otros, matricula)
            print("Revisión insertada exitosamente.")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejemplo de uso
if __name__ == "__main__":
    create_tables()
    if login_menu():
        menu()
