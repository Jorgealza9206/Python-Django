# Profundizar en el uso de sets
# Un set es la colección de elementos únicos y además es mutable
# Los elementos de un set deben ser inmutables   Es decir no deben tener listas, solo strings, integers, floats, etc

# conjunto = {[1,2],[3,4],[5,6],[7,8]}
conjunto = {'Juan' ,True, 18.0}
print(conjunto)
# Set vacío
# conjunto = {} Esto genera un diccionario vacío
# print(type(conjunto))
# set vacío correcto
conjunto = set()
print(conjunto)
print(type(conjunto))
# Mutable
conjunto.add('Juan')
print(conjunto)
# Contiene valores únicos, es decir, no se agrega sino al haber ya uno, no agrega nada
conjunto.add('Juan')
print(conjunto)
# Crear un set a partir de un iterable
conjunto = set([1,9,5,8,9]) # Quita el valor duplicado
print(conjunto)
# Podemos agregar más elementos o incluso otro set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2) # Agrega los elementos del conjunto2 al conjunto1
print(conjunto)
conjunto.update([20,30,40,40]) # Podemos agregar incluso una lista
print(conjunto)

# Copiar un set (Copia poco profunda, solo copia las referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar la igualdad
print(f'¿Es igual en contenido?: {conjunto == conjunto_copia}')
print(f'¿Es la misma referencia?: {conjunto is conjunto_copia}')

#Operaciones de conjuntos utilizando set
#Personas con distintas características

pelo_negro = {'Juan','Carla', 'Pedro','Maria'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Carla','Laura'}
menores_30 = {'Juan','Carla','Maria'}
#Todos los elementos de color cafe y pelo rubio (Union) (No se repiten elementos)
print(ojos_cafe.union(pelo_rubio))
#Invertir el orden con el mismo resultado
print(pelo_rubio.union(ojos_cafe))

#Intersección - Sólo las personas de color café y pelo rubio (Es conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# (difference) Personas con pelo negro que no tienen ojos café (No conmutativa)
print(pelo_negro.difference(ojos_cafe))

# (Diferencia simétrica) Personas con pelo negro y que no tienen ojos café (Conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))
