import flet as ft


def registrar_evento_cierre(page: ft.Page):

    def cerrar_dialogo(e=None):
        dialog.open = False
        page.update()

    async def cerrar_aplicacion(e):

        await page.window.destroy()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            controls=[
                ft.Icon(
                    ft.Icons.EXIT_TO_APP,
                    color=ft.Colors.RED
                ),
                ft.Text(
                    "Salir del sistema",
                    weight=ft.FontWeight.BOLD
                )
            ],
            tight=True
        ),
        content=ft.Text(
            "¿Desea cerrar el programa?"
        ),
        actions=[
            ft.TextButton(
                "No",
                on_click=cerrar_dialogo
            ),
            ft.ElevatedButton(
                "Sí",
                icon=ft.Icons.CHECK,
                on_click=cerrar_aplicacion
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    async def confirmar_cierre(e: ft.WindowEvent):

        if e.type != ft.WindowEventType.CLOSE:
            return

        dialog.open = True
        page.show_dialog(dialog)

    page.window.prevent_close = True
    page.window.on_event = confirmar_cierre