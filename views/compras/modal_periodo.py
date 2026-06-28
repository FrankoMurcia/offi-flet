import flet as ft
from datetime import datetime

from models.periodo import Periodo

def mostrar_modal_periodo(page,state,dd_periodos,nombre_periodo_actual,btn_nueva_factura,seleccionar_periodo,cargar,mostrar_error,):
    

    def cerrar_modal(dialog):
        dialog.open = False
        page.update()

    def abrir_modal_crear_periodo(e=None):

        txt_nuevo_periodo = ft.TextField(
            label="Nombre período",
            width=250
        )

        dd_anio = ft.Dropdown(
            label="Año",
            width=150,
            options=[
                ft.dropdown.Option(str(anio))
                for anio in range(
                    datetime.now().year - 5,
                    datetime.now().year + 6
                )
            ]
        )

        def guardar_periodo(e):

            if not txt_nuevo_periodo.value.strip():
                mostrar_error(
                    "Validación",
                    "Debe ingresar un nombre."
                )
                return

            if not dd_anio.value:
                mostrar_error(
                    "Validación",
                    "Debe seleccionar un año."
                )
                return

            Periodo.guardar(
                txt_nuevo_periodo.value.strip(),
                int(dd_anio.value)
            )

            dialog_crear.open = False

            seleccionar_periodo()

            periodos = Periodo.obtener_todos()

            if periodos:
                dd_periodos.value = str(periodos[-1][0])

            page.update()

        dialog_crear = ft.AlertDialog(
            modal=True,
            title=ft.Text("Crear período"),
            content=ft.Column(
                [
                    txt_nuevo_periodo,
                    dd_anio
                ],
                tight= True
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: cerrar_modal(dialog_crear)
                ),
                ft.ElevatedButton(
                    "Guardar",
                    on_click=guardar_periodo
                )
            ]
        )

        page.show_dialog(dialog_crear)

    def usar_periodo(e):

        if not dd_periodos.value:
            mostrar_error(
                "Período requerido",
                "Debe seleccionar un período."
            )
            return

        state.periodo_actual = int(
            dd_periodos.value
        )

        periodo = Periodo.obtener_por_id(
            state.periodo_actual
        )

        nombre_periodo_actual.value = f"{periodo[1]} - {periodo[2]}"

        btn_nueva_factura.disabled = False

        modal_periodo.open = False

        cargar()

        page.update()
    
    modal_periodo = None

    def abrir_modal_periodo():

        nonlocal modal_periodo

        modal_periodo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Seleccionar Período"),
            content=ft.Container(
                width=350,
                content=dd_periodos
            ),
            actions=[
                ft.TextButton(
                    "Crear",
                    on_click=abrir_modal_crear_periodo
                ),
                ft.ElevatedButton(
                    "Usar",
                    on_click=usar_periodo
                )
            ]
        )

        page.show_dialog(modal_periodo)
    
    abrir_modal_periodo()

def crear_nombre_periodo():

    return ft.Text(
        "Sin período seleccionado",
        size=18,
        weight=ft.FontWeight.BOLD
    )