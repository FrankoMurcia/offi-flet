import flet as ft
from views.compras.validaciones import mostrar_error


def cerrar_dialogo(dialog, page):

    dialog.open = False
    page.update()


def mostrar_alerta(page: ft.Page, titulo: str, mensaje: str):

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(titulo),
        content=ft.Text(mensaje),
    )

    dialog.actions = [
        ft.TextButton(
            "Aceptar",
            on_click=lambda e: cerrar_dialogo(dialog, page)
        )
    ]

    page.show_dialog(dialog)



def mostrar_confirmacion(page: ft.Page, titulo: str, mensaje: str, accion):

    dialog_confirmacion = ft.AlertDialog(
        modal=True,
        title=ft.Text(titulo),
        content=ft.Text(mensaje),
    )


    def confirmar(e):

        dialog_confirmacion.open = False
        page.update()

        accion()


    dialog_confirmacion.actions = [
        ft.TextButton(
            "Cancelar",
            on_click=lambda e: (
                setattr(dialog_confirmacion, "open", False),
                page.update()
            )
        ),
        ft.TextButton(
            "Confirmar",
            on_click=confirmar
        )
    ]

    page.show_dialog(dialog_confirmacion)



def mostrar_exito(page: ft.Page, titulo: str, mensaje: str):

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            [
                ft.Icon(
                    ft.Icons.CHECK_CIRCLE,
                    color=ft.Colors.GREEN,
                ),
                ft.Text(titulo)
            ]
        ),
        content=ft.Text(mensaje),
    )


    dialog.actions = [
        ft.FilledButton(
            "Aceptar",
            on_click=lambda e: cerrar_dialogo(dialog,page)
        )
    ]


    page.show_dialog(dialog)



def mostrar_mensaje(page: ft.Page, texto: str):
    mostrar_error(page, "Aviso", texto)