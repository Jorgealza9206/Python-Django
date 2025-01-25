# nombre = 'Jorge'
# edad = 32
# mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre,edad)
# print(mensaje_con_formato)

# persona = ('Karla', 'Gomez', 5000.00)
# # mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.f'%persona
# # print(mensaje_con_formato)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)

nombre = 'Jorge'
edad = 32
sueldo = 3000000
# mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje_con_formato)

mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre, edad, sueldo)
print(mensaje)