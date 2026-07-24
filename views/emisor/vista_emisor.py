import flet as ft

#from views.emisor.dialog_manager import cerrar_dialogo, abrir_dialogo
from .formularios import FormularioEmisor
from .dialogos import mostrar_confirmacion, mostrar_exito
from .tabla import construir_tabla, cargar_filas
from .handlers import guardar_emisor, eliminar_emisor


def vista_emisor(page: ft.Page):

    tabla = construir_tabla()
    id_edicion = None

    def recargar():
        cargar_filas(page, tabla, on_editar=abrir_modal, on_eliminar=on_eliminar)

    def on_eliminar(id_emisor):
        eliminar_emisor(page, id_emisor, recargar)

    def abrir_modal(emisor=None):

        nonlocal id_edicion
        form = FormularioEmisor()

        if emisor:
            id_edicion = emisor[0]
            form.cargar_emisor(emisor)
            titulo = "Editar Emisor"
            texto_boton = "Actualizar"
        else:
            id_edicion = None
            form.limpiar()
            titulo = "Nuevo Emisor"
            texto_boton = "Guardar"

        def limpiar_id():
            nonlocal id_edicion
            id_edicion = None

        def cerrar_modal(e):
            dialog_emisor.open = False
            page.update()

        def on_guardar(e):
            guardar_emisor(page, form, id_edicion, dialog_emisor, recargar, limpiar_id, mostrar_exito_callback,)

        ancho_modal = min(850, page.width - 60) if page.width else 850

        dialog_emisor = ft.AlertDialog(
            modal=True,
            title=ft.Row(
                [
                    ft.Icon(
                        ft.Icons.BUSINESS,
                        color=ft.Colors.BLUE,
                        size=30,
                    ),
                    ft.Text(
                        titulo,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
            ),
            content=ft.Container(
                width=ancho_modal,
                height=520,
                padding=20,
                content=form.construir_formulario(),
            ),
            actions_alignment=ft.MainAxisAlignment.END,
            actions=[
                ft.OutlinedButton(
                    "Cancelar",
                    icon=ft.Icons.CLOSE,
                    on_click=cerrar_modal,
                ),
                ft.FilledButton(
                    texto_boton,
                    icon=ft.Icons.SAVE,
                    on_click=on_guardar,
                ),
            ],
        )
        page.show_dialog(dialog_emisor)

        def mostrar_exito_callback():
            if id_edicion is None:
                mostrar_exito(
                    page,
                    "Éxito",
                    "Emisor guardado correctamente."
                )
            else:
                mostrar_exito(
                    page,
                    "Éxito",
                    "Emisor actualizado correctamente."
                )

    btn_nuevo = ft.ElevatedButton(
        content=ft.Text("Nuevo Emisor"),
        icon=ft.Icons.ADD,
        on_click=lambda e: abrir_modal()
    )

    recargar()

    return ft.Container(
        padding=ft.Padding(top=10, left=0, right=0, bottom=0),
        content=ft.Column(
            [
                ft.Container(height=9),
                ft.Row(
                    [ft.Text("Gestión de Emisores", size=30, weight=ft.FontWeight.BOLD), btn_nuevo],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(height=30),
                ft.Text("Listado de Emisores", size=20, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row([ft.Text("Emisores registrados", weight=ft.FontWeight.BOLD)]),
                            ft.Divider(),
                            ft.Row([tabla], scroll=ft.ScrollMode.AUTO)
                        ]
                    ),
                    padding=20,
                    border_radius=15,
                    bgcolor=ft.Colors.BLUE_GREY_900
                )
            ],
            expand=True,
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )
    )