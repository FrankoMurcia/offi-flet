import flet as ft
import asyncio
from views.compras.validaciones import mostrar_error, mostrar_exito


def mostrar_mensaje(page, texto):
    mostrar_error(page, "Aviso", texto)


def mostrar_confirmacion(page, titulo, mensaje, accion):

    dialog = None

    def cerrar(e=None):
        dialog.open = False
        page.update()

    def confirmar(e):

        cerrar()

        async def ejecutar():
            await asyncio.sleep(0.1)
            accion()

        page.run_task(ejecutar)

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(titulo),
        content=ft.Text(mensaje),
        actions=[
            ft.TextButton(
                "Cancelar",
                on_click=cerrar
            ),
            ft.ElevatedButton(
                "Confirmar",
                icon=ft.Icons.CHECK,
                on_click=confirmar
            )
        ]
    )

    page.show_dialog(dialog)