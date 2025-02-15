# nombre = 'Jorge'
# edad = 32
# mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre,edad)
# print(mensaje_con_formato)

# persona = ('Karla', 'Gomez', 5000.00)
# # mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.f'%persona
# # print(mensaje_con_formato)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)

# nombre = 'Jorge'
# edad = 32
# sueldo = 3000000
# mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje_con_formato)

# mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre, edad, sueldo)
# # print(mensaje)
#
# mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# # print(mensaje)
#
# diccionario = {'nombre':'Iván','edad':35, 'sueldo':5000.00}
# mensaje = 'Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]:.2f}'.format(persona=diccionario)
# print(mensaje)

#f-string
# mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
# print(mensaje)
#
# print(nombre, edad, sueldo)

#multiplicación de str

#carácteres de escape
# resultado = 'Hola \' Mundo\''
# print(resultado)

# resultado = 'Se va a eliminar el .\b'
# print(resultado)

#Caracter \

# resultado = 'c:\\directorio\\juamn'
# print(resultado)

#raw string
resultado = r'Cadena con \n salto de linea'
print(resultado)
