import flet as ft

from auth.controls import LoginControls


def crear_controles():

    controls = LoginControls()

    controls.txt_usuario = ft.TextField(

        label="Usuario",

        prefix_icon=ft.Icons.PERSON,

        width=320

    )

    controls.txt_contraseña = ft.TextField(

        label="Contraseña",

        password=True,

        can_reveal_password=True,

        prefix_icon=ft.Icons.LOCK,

        width=320

    )

    controls.lbl_error = ft.Text(

        "",

        color=ft.Colors.RED

    )

    return controls