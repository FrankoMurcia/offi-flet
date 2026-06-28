import flet as ft

from models.Clasificaciones.clasificacion import Clasificacion
from models.Clasificaciones.sector import Sector
from models.Clasificaciones.tipo_costo_gasto import TipoCostoGasto
from models.Clasificaciones.tipo_operacion import TipoOperacion
from views.compras.clasificacion_service import actualizar_textos

def mostrar_modal_clasificacion(page, state, controls):

    dd_clasificacion = ft.Dropdown(
        label="Clasificación",
        width=250
    )

    dd_sector = ft.Dropdown(
        label="Sector",
        width=250
    )

    dd_tipo_costo = ft.Dropdown(
        label="Tipo Costo/Gasto",
        width=250
    )

    dd_tipo_operacion = ft.Dropdown(
        label="Tipo Operación",
        width=250
    )

    dd_clasificacion.options = [
        ft.dropdown.Option(
            key=str(id_),
            text= f"{id_}. {descripcion}"
        )
        for id_, descripcion in Clasificacion.obtener_todos()
    ]

    dd_sector.options = [
        ft.dropdown.Option(
            key=str(id_),
            text=f"{id_}. {descripcion}"
        )
        for id_, descripcion in Sector.obtener_todos()
    ]

    dd_tipo_costo.options = [
        ft.dropdown.Option(
            key=str(id_),
            text=f"{id_}. {descripcion}"
        )
        for id_, descripcion in TipoCostoGasto.obtener_todos()
    ]

    dd_tipo_operacion.options = [
        ft.dropdown.Option(
            key=str(id_),
            text=f"{id_}. {descripcion}"
        )
        for id_, descripcion in TipoOperacion.obtener_todos()
    ]

    if state.clasificacion_seleccionada:
        dd_clasificacion.value = str(state.clasificacion_seleccionada)

    if state.sector_seleccionado:
        dd_sector.value = str(state.sector_seleccionado)

    if state.tipo_costo_gasto_seleccionado:
        dd_tipo_costo.value = str(state.tipo_costo_gasto_seleccionado)

    if state.tipo_operacion_seleccionado:
        dd_tipo_operacion.value = str(state.tipo_operacion_seleccionado)

    def cerrar_modal(dialog):
        dialog.open = False
        page.update()

    # txt_clasificacion.value = str(state.clasificacion_seleccionada) if state.clasificacion_seleccionada else None
    # txt_sector.value = str(state.sector_seleccionado) if state.sector_seleccionado else None
    # txt_tipo_costo.value = str(state.tipo_costo_gasto_seleccionado) if state.tipo_costo_gasto_seleccionado else None
    # txt_tipo_operacion.value = str(state.tipo_operacion_seleccionado) if state.tipo_operacion_seleccionado else None

    def aceptar(e):

        if not dd_clasificacion.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Debe seleccionar una Clasificación")
            )
            page.snack_bar.open = True
            page.update()
            return

        if not dd_sector.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Debe seleccionar un Sector")
            )
            page.snack_bar.open = True
            page.update()
            return

        if not dd_tipo_costo.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Debe seleccionar un Tipo de Costo/Gasto")
            )
            page.snack_bar.open = True
            page.update()
            return

        if not dd_tipo_operacion.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Debe seleccionar un Tipo de Operación")
            )
            page.snack_bar.open = True
            page.update()
            return

        # guardar estados
        state.clasificacion_seleccionada = int(dd_clasificacion.value or 0)
        state.sector_seleccionado = int(dd_sector.value or 0)
        state.tipo_costo_gasto_seleccionado = int(dd_tipo_costo.value or 0)
        state.tipo_operacion_seleccionado = int(dd_tipo_operacion.value or 0)

        actualizar_textos(state, controls)

        # textos
        # txt_clasificacion.value = next(o.text for o in dd_clasificacion.options if o.key == dd_clasificacion.value)
        # txt_sector.value = next(o.text for o in dd_sector.options if o.key == dd_sector.value)
        # txt_tipo_costo.value = next(o.text for o in dd_tipo_costo.options if o.key == dd_tipo_costo.value)
        # txt_tipo_operacion.value = next(o.text for o in dd_tipo_operacion.options if o.key == dd_tipo_operacion.value)

        dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Clasificación Fiscal"),
        content=ft.Container(
            width=700,
            height=300,
             padding=20,
            content=ft.Column([
                 ft.Row([
                    dd_tipo_operacion,
                    dd_clasificacion,
                 ]),
                 ft.Row([
                    dd_tipo_costo,
                    dd_sector,
                 ])
             ]),
          ),
        actions=[
            ft.TextButton(
                "Cancelar",
                on_click=lambda e: cerrar_modal(dialog)
            ),
            ft.ElevatedButton(
                "Aceptar",
                on_click=aceptar
            )
        ]
    )

    page.show_dialog(dialog)
    page.update()
