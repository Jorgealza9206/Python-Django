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