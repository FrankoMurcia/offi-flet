import flet as ft

from auth import session


def cerrar_sesion(page: ft.Page, mostrar_login):

    def cancelar(e):

        dialog.open = False
        page.update()

    def aceptar(e):

        # Cierra la sesión actual
        session.cerrar()

        # Cierra el diálogo
        dialog.open = None

        # Regresa al Login
        mostrar_login()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            controls=[
                ft.Icon(
                    ft.Icons.LOGOUT,
                    color=ft.Colors.ORANGE
                ),
                ft.Text(
                    "Cerrar sesión",
                    weight=ft.FontWeight.BOLD
                )
            ],
            tight=True
        ),
        content=ft.Text(
            "¿Desea cerrar la sesión actual?"
        ),
        actions=[
            ft.TextButton(
                "Cancelar",
                on_click=cancelar
            ),
            ft.ElevatedButton(
                "Cerrar sesión",
                icon=ft.Icons.LOGOUT,
                on_click=aceptar
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.show_dialog(dialog)