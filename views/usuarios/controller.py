from views.usuarios.state import UsuarioState
from views.usuarios.control_factory import crear_controles


class UsuarioController:

    def __init__(self, page):

        self.page = page

        self.state = UsuarioState()

        self.controls = None

    def crear_controles(self):

        self.controls = crear_controles(self.page)