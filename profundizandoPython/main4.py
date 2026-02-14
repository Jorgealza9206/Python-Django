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
print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo)+10,'-'))

#Alinea hacia la derecha
print(titulo.rjust(len(titulo)+10,'-'))