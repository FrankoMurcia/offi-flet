import flet as ft


def mostrar_alerta(page: ft.Page, titulo: str, mensaje: str):
    def cerrar(e):
        dialog_alerta.open = False

    dialog_alerta = ft.AlertDialog(
        modal=True,
        title=ft.Text(titulo),
        content=ft.Text(mensaje),
        actions=[ft.TextButton("Aceptar", on_click=cerrar)]
    )
    page.show_dialog(dialog_alerta)


def mostrar_confirmacion(page: ft.Page, titulo: str, mensaje: str, accion):
    def cerrar_modal(dialog):
        dialog.open = False
        page.update()

    def confirmar(e):
        cerrar_modal(dialog_confirmacion)
        accion()

    dialog_confirmacion = ft.AlertDialog(
        modal=True,
        title=ft.Text(titulo),
        content=ft.Text(mensaje),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: cerrar_modal(dialog_confirmacion)),
            ft.TextButton("Confirmar", on_click=confirmar)
        ]
    )
    page.show_dialog(dialog_confirmacion)


def mostrar_mensaje(page: ft.Page, texto: str):
    page.snack_bar = ft.SnackBar(content=ft.Text(texto))
    page.snack_bar.open = True
    page.update()