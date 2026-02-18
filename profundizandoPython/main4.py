mensaje = 'Hola mundo'
# print(mensaje.lower().islower())
# print(mensaje.isupper())
# print(mensaje.upper().isupper())

#Alinear cadenas

# center - Centrar un string
titulo = 'Sitio web de JorgeAlza.com.co'
#print(len(titulo))
# print(titulo.center(50,'*'))
# print(len(titulo.center(50,'*')))
# print(titulo.center(len(titulo)+10,'-'))

#ljust -Alinea a la izquierda
# print(titulo.ljust(50,'*'))
# print(titulo.ljust(len(titulo)+10,'-'))
#
# #Alinea hacia la derecha
# print(titulo.rjust(len(titulo)+10,'-'))

#Reemplazar
print(titulo.replace(' ','-'))

#Eliminar caracteres al inicio y al final
titulo = ' ***GlobalMentoring.com.mx*** '
print('Cadena original:', titulo, len(titulo))
titulo = titulo.strip() #Quita espacios al inicio y al final
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*') #Quita todos los asteriscos a la der e izq
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:', titulo, len(titulo))

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip() #Quita primero espacios y luego asteriscos
print('Cadena modificada:', titulo, len(titulo))
