#Profundizando en el tipo str

# carácteres bytes

caracteres_en_bytes = b'Hola mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

#Convertir de str a bytes
string = 'Programación con Python'
print(string)

bytes = string.encode('utf-8')
print(bytes)

#Convertir de bytes a string
string2 = bytes.decode('utf-8')
print(string2)

print(string == string2)