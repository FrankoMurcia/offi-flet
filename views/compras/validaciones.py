from datetime import datetime
from models.compras import Factura
import flet as ft

def validar_factura_existente(controls, mostrar_error):

        if (
            controls.txt_fecha.value and
            controls.txt_codigo_generacion.value and
            controls.txt_subtotal.value
        ):

            try:
                fecha_sql = datetime.strptime(
                    controls.txt_fecha.value,
                    "%d-%m-%Y"
                ).strftime("%Y-%m-%d")

                subtotal = float(
                    controls.txt_subtotal.value.replace(",", "")
                )

                if Factura.existe_compra(
                    controls.txt_codigo_generacion.value,
                ):
                    mostrar_error(
                        "Factura duplicada",
                        "Esta compra ya se encuentra registrada."
                    )
            except Exception as ex:
                print(ex)

def validar_guardado(state, controls, mostrar_error, page):

    if state.periodo_actual is None:
        mostrar_error(
            page,
            "Validación",
            "Debe seleccionar un período"
        )
        return False

    if not controls.dd_tipo_documento.value:
        mostrar_error(
            page,
            "Validación",
            "Debe seleccionar tipo de documento"
        )
        return False

    if not controls.dd_emisor.value:
        mostrar_error(
            page,
            "Validación",
            "Debe seleccionar un emisor"
        )
        return False

    if not controls.dd_clase_documento.value:
        mostrar_error(
            page,
            "Validación",
            "Debe seleccionar clase de documento"
        )
        return False

    return True

def validar_dropdown(control, mensaje, mostrar_error, page):
    if not control.value:
        mostrar_error(
            page,
            "Validación",
            mensaje
        )
        return False
    return True

def mostrar_error(page,titulo,mensaje):
    page.snack_bar = ft.SnackBar(
        content=ft.Text(f"{titulo}: {mensaje}"),
        open=True
    )
    page.snack_bar.open = True
    page.update()