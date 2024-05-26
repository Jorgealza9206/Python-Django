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
            sentencia = 'UPDATE persona SET  nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan','Perez','jperez@mail.com',1),
                ('Ivonne', 'Gutierrez', 'igutierrez@mail.com', 2)
            )
            cursor.executemany(sentencia, valores)
            #conexion.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()