#concatenacion cadenas de carateres con contenidos de variables

nombre="Burciaga Acosta Edgar Antonio"
especialidad="Area de Desarrollo de SW Multiplataforma"
carrea="Ingeniero en gestion y desarrollo de SW"

#1er froma de concatenar
print("Mi nombre es: "+nombre+" estoy en la especialidad de: "+especialidad+" en la carrera de: "+carrea)

print("/n")
#2da froma de concatenar
print("Mi nombre es: ",nombre," estoy en la especialidad de: ",especialidad," en la carrera de: ",carrea)

print("/n")
#3er froma de concatenar
print(f"Mi nombre es: {nombre} estoy en la especialidad de: {especialidad} en la carrera de: {carrea}")

print("/n")
#4ta froma de concatenar
print("Mi nombre es: {} estoy en la especialidad de: {} en la carrera de: {}".format(nombre,especialidad,carrea))

#5ta froma de concatenar
print('Mi nombre es: '+nombre+'estoy en la especialidad de: '+especialidad+' en la carrera de: '+carrea)