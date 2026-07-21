import flet as ft


def cerrar_dialog(dialog, page):
    if dialog is not None:
        dialog.open = False

    if getattr(page, "dialog", None) is dialog:
        page.dialog = None

    page.update()

def mostrar_error( page, titulo, mensaje):

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton(
                    "Aceptar",
                    on_click=lambda e: cerrar_dialog(dialog, page)
                )
            ]
        )
        page.show_dialog(dialog)

def mostrar_mensaje(page, texto):

        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto)
        )

        page.snack_bar.open = True
        page.update()

def mostrar_confirmacion(page, titulo, mensaje, accion):

        def confirmar(e):
            dialog.open = False
            page.update()
            accion()

        def cancelar(e):
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=cancelar
                ),
                ft.TextButton(
                    "Confirmar",
                    on_click=confirmar
                )
            ]
        )

        page.show_dialog(dialog)