archivo = open('prueba.txt','r',encoding='utf-8')

#print(archivo.read())

#leer algunos caracteres
#print(archivo.read(5))
#print(archivo.read(3))

#Leer lineas completas

#print(archivo.readline())
#print(archivo.readline())

#iterar el archivo

# for linea in archivo:
#     print(linea)

#Leer lineas

#print(archivo.readlines()[1])

#abrimos nuevo archivo

archivo2 = open('copia.txt','a', encoding='utf-8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se ha terminado el proceso de leer y copiar')