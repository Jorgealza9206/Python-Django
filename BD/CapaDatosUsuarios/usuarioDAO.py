from usuario import Usuario
from cursor_del_pool import CursorDelPool
from logger_base import log

class UsuarioDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO USUARIO(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        # with Conexion.obtenerConexion() as conexion:
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            log.debug(usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'usuario insertado: {usuario}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'usuario actualizado: {usuario}')
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar un registro
    usuario1 = Usuario(username='Valentina', password='Londoño1234')
    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Usuarios insertados: {usuarios_insertados}')

    # #Actualizar registro
    # usuario1 = Usuario(22,'Victor','Casachahua','vcasachahua@mail.com')
    # usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    # log.debug(f'Usuarios actualizados: {usuarios_actualizados}')
    #
    # #Eliminar un registro
    # usuario1 = Usuario(id_usuario=11)
    # usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Usuarios eliminados: {usuarios_eliminados}')

    #Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)