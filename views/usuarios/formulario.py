import flet as ft


def crear_formulario(controls):

    return ft.Column(

        [

            controls.txt_usuario,

            controls.txt_contraseña,

            controls.txt_nombre,

            controls.dd_rol

        ],

        tight=True,

        spacing=15

    )