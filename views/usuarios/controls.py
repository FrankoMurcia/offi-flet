import flet as ft


class UsuarioControls:

    def __init__(self):

        self.txt_usuario: ft.TextField | None = None

        self.txt_contraseña: ft.TextField | None = None

        self.txt_nombre: ft.TextField | None = None

        self.dd_rol: ft.Dropdown | None = None