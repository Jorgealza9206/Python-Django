from logger_base import log

class Usuario:

    def __init__(self, id_usuario = None, username = None, password = None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'Id: {self._id_usuario}, username: {self._username}, password: {self._password}'