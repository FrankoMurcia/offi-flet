import flet as ft

from auth.control_factory import crear_controles
from auth import session
from auth.login_controller import LoginController


def vista_login(page, al_ingresar):

    controller = LoginController()

    controls = crear_controles()

    def ingresar(e):

        usuario = controls.txt_usuario.value.strip()

        contraseña = controls.txt_contraseña.value

        if not usuario:

            controls.lbl_error.value = "Ingrese el usuario."

            page.update()

            return

        if not contraseña:

            controls.lbl_error.value = "Ingrese la contraseña."

            page.update()

            return

        usuario_logueado = controller.login(
            usuario,
            contraseña
        )

        if usuario_logueado is None:

            controls.lbl_error.value = "Usuario o contraseña incorrectos."

            controls.txt_contraseña.value = ""

            #controls.txt_contraseña.focus()

            page.update()

            return

        session.iniciar(usuario_logueado)
        
        controls.lbl_error.value = ""

        page.update()

        al_ingresar()

    controls.btn_ingresar = ft.ElevatedButton(

        "Ingresar",

        width=320,

        on_click=ingresar
)

    return ft.Container(
        expand=True,
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Card(
                            elevation=8,
                            content=ft.Container(
                                width=420,
                                padding=30,
                                content=ft.Column(
                                    [
                                        ft.Icon(
                                            ft.Icons.ACCOUNT_CIRCLE,
                                            size=70,
                                        ),

                                        ft.Text(
                                            "Sistema Contable",
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                        ),

                                        ft.Text(
                                            "Iniciar sesión",
                                            size=16,
                                        ),

                                        controls.txt_usuario,
                                        controls.txt_contraseña,
                                        controls.btn_ingresar,
                                        controls.lbl_error,
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20,
                                    tight=True,
                                ),
                            ),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
    )