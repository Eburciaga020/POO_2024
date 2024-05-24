captura= "si"
pacientes = 0

while captura == "si":
    nombre_paciente = input("Ingresa tu nombre: ")
    tipo_sangre = input("Tipo de sangre: ")
    
    ps1 = int(input("Ingrese la primera medición de la presión sistólica: "))
    pd1 = int(input("Ingrese la primera medición de la presión diastólica: "))
    
    ps2 = int(input("Ingrese la segunda medición de la presión sistólica: "))
    pd2 = int(input("Ingrese la segunda medición de la presión diastólica: "))
    
    ps3 = int(input("Ingrese la tercera medición de la presión sistólica: "))
    pd3 = int(input("Ingrese la tercera medición de la presión diastólica: "))

    md = int(input("Ingrese la medición final de la presión diastólica: "))
    ms = int(input("Ingrese la medición final de la presión sistólica: "))
    
    print(f"Primera medición: {ps1}, {pd1}")
    print(f"Segunda medición: {ps2}, {pd2}")
    print(f"Tercera medición: {ps3}, {pd3}")
    
    psf = (ps1 + ps2 + ps3) / 3 
    pdf = (pd1 + pd2 + pd3) / 3

    print("Presion sistolica promedio: ",psf)
    print("Presion diastolica promedio: ",pdf)
    
    if psf <= 120 and pdf <= 80:
        print("Presenta una presión normal")
    
    pacientes += 1
    
    captura = input("¿Desea realizar otra captura? (si/no): ")

print(f"Total de pacientes capturados: {pacientes}")