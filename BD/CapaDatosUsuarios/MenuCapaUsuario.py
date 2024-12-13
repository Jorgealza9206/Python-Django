from usuarioDAO import UsuarioDAO
from logger_base import log
from usuario import Usuario

def listarUsuarios():
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.info(usuario)

def insertarUsuario():
    try:
        entrada = input("Ingresa el username y password separados por coma\n")
        tupla = tuple(item.strip() for item in entrada.split(","))
        usuario, contraseña = tupla
        usuario1 = Usuario(username=usuario, password=contraseña)
        usuarios_insertados = UsuarioDAO.insertar(usuario1)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    except:
        log.info("Valor mal ingresado, intente nuevamente")

def actualizarUsuario():
    try:
        entrada = input("Ingresa el id, username y password separados por coma a actualizar\n")
        tupla = tuple(item.strip() for item in entrada.split(","))
        id, usuario, contraseña = tupla
        usuario1 = Usuario(id, usuario, contraseña)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    except:
        log.info("Valor mal ingresado, intente nuevamente")

def eliminarUsuario():
    try:
        entrada = int(input("Ingresa el id del usuario a eliminar\n"))
        usuario1 = Usuario(id_usuario=entrada)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
    except:
        log.info("Valor mal ingresado, intente nuevamente")

if __name__ == '__main__':
    opcion = None
    while opcion != 5:
        print('Seleccione alguna opción')
        opcion = int(input("""
        1. Listar usuarios
        2. Insertar usuario
        3. Modificar usuario
        4. Eliminar usuario
        5. Salir
        """))
        if opcion == 1:
            listarUsuarios()
        elif opcion == 2:
            insertarUsuario()
        elif opcion == 3:
            actualizarUsuario()
        elif opcion == 4:
            eliminarUsuario()
    else:
        print("Salimos de la aplicación")