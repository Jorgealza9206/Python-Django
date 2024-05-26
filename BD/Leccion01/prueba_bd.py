import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port = '5432',
    database='test_db'
)
print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT *  FROM persona WHERE id_persona IN %s'
            #llaves_primarias = ((1,2,3),)
            entrada = input('Proporciona los id\' a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),) #Divide cada entrada separada por comas y la convierte en tupla
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()