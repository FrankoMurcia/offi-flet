import flet as ft

from models.emisor import Emisor
from models.Clasificaciones.tipo_documento import TipoDocumento
from models.Clasificaciones.clase_documento import ClaseDocumento
from models.periodo import Periodo

def seleccionar_periodo(dd_periodos):

        dd_periodos.options = [
            ft.dropdown.Option(
                key=str(p[0]),
                text=f"{p[2]} - {p[3]}"
            )
            for p in Periodo.obtener_todos()
        ]

def cargar_dropdowns(state, controls, dd_periodos):

        state.emisores_cache = Emisor.obtener_todos()

        controls.dd_emisor.options= [
            ft.dropdown.Option(
                key = str(e[0]),
                text= e[1]
            )
            for e in state.emisores_cache
        ]

        controls.dd_tipo_documento.options = [
            ft.dropdown.Option(
                key=str(t[0]),
                text=f"{t[0]}. {t[1]}"
            )
            for t in TipoDocumento.obtener_todos()
        ]

        controls.dd_clase_documento.options = [
            ft.dropdown.Option(
                key=str(id__),
                text=f"{id__}. {descripcion}"
            )
            for id__, descripcion in ClaseDocumento.CLASE_DOCUMENTO.items()
        ]

        seleccionar_periodo(dd_periodos)

def crear_dropdown_periodos():
    return ft.Dropdown(
        label="Período",
        width=300
    )