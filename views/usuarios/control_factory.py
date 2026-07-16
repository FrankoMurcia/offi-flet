import flet as ft

from views.usuarios.controls import UsuarioControls


def crear_controles(page):

    controls = UsuarioControls()

    controls.txt_usuario = ft.TextField(
        label="Usuario",
        width=300
    )

    controls.txt_contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=300
    )

    controls.txt_nombre = ft.TextField(
        label="Nombre completo",
        width=400
    )

    controls.dd_rol = ft.Dropdown(
        label="Rol",
        width=250,
        options=[
            ft.dropdown.Option("Administrador"),
            ft.dropdown.Option("Cliente"),
        ]
    )

    return controls