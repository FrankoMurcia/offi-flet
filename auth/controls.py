import flet as ft


class LoginControls:

    def __init__(self):

        self.txt_usuario: ft.TextField | None = None

        self.txt_contraseña: ft.TextField | None = None

        self.btn_ingresar: ft.ElevatedButton | None = None

        self.lbl_error: ft.Text | None = None