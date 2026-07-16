import flet as ft


def mostrar_error(page, titulo, mensaje):

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(titulo),
        content=ft.Text(mensaje),
        actions=[
            ft.TextButton(
                "Aceptar",
                on_click=lambda e: cerrar()
            )
        ]
    )

    def cerrar():
        dialog.open = False
        page.update()

    page.show_dialog(dialog)

def mostrar_confirmacion(page, titulo, mensaje, accion):

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(titulo),
        content=ft.Text(mensaje),
        actions=[
            ft.TextButton(
                "Cancelar",
                on_click=lambda e: cerrar()
            ),
            ft.ElevatedButton(
                "Aceptar",
                on_click=lambda e: confirmar()
            )
        ]
    )

    def cerrar():
        dialog.open = False
        page.update()

    def confirmar():
        dialog.open = False
        page.update()
        accion()

    page.show_dialog(dialog)