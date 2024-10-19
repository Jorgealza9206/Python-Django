from usuarioDAO import UsuarioDAO
from logger_base import log
from usuario import Usuario

def listarUsuarios():
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)

def insertarUsuario():
    entrada = input("Ingresa el username y password separados por coma")
    usuario1 = Usuario(username='Valentina', password='Londoño1234')
    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Usuarios insertados: {usuarios_insertados}')

if __name__ == '__main__':
    print('Seleccione alguna opción')
    opcion = int(input("""1. Listar usuarios
    2. Insertar usuario
    3. Modificar usuario
    4. Eliminar usuario
    """))
    if opcion == 1:
        listarUsuarios()