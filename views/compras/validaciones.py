from datetime import datetime
import flet as ft
import re

from models.compras import Factura


# ==========================================================
# VALIDACIONES
# ==========================================================

def validar_fecha(controls, mostrar_error):

    fecha = (controls.txt_fecha.value or "").strip()

    if not fecha:
        mostrar_error(
            "Validación",
            "Debe ingresar una fecha."
        )
        return False

    try:
        datetime.strptime(fecha, "%d-%m-%Y")
    except ValueError:
        mostrar_error(
            "Validación",
            "La fecha debe tener el formato dd-mm-yyyy."
        )
        return False

    return True

PATRON_CODIGO_GENERACION = re.compile(
    r"^[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}$",
    re.IGNORECASE,
)


def validar_codigo_generacion(controls, mostrar_error):

    codigo = (controls.txt_codigo_generacion.value or "").strip()

    if not codigo:
        mostrar_error(
            "Validación",
            "Debe ingresar el Código de Generación."
        )
        return False

    if len(codigo) < 36:
        return False

    if not PATRON_CODIGO_GENERACION.fullmatch(codigo):
        mostrar_error(
            "Validación",
            "El Código de Generación no es válido."
        )
        return False

    return True

def validar_subtotal(controls, mostrar_error):

    subtotal_texto = (
        controls.txt_subtotal.value or ""
    ).replace(",", "").strip()

    if not subtotal_texto:
        mostrar_error(
            "Validación",
            "Debe ingresar el Subtotal."
        )
        return False

    try:
        subtotal = float(subtotal_texto)
    except ValueError:
        mostrar_error(
            "Validación",
            "El Subtotal debe ser un número válido."
        )
        return False

    if subtotal <= 0:
        mostrar_error(
            "Validación",
            "El Subtotal debe ser mayor que cero."
        )
        return False

    return True

def validar_factura_existente(controls, mostrar_error, page):

    if (
        controls.txt_fecha.value
        and controls.txt_codigo_generacion.value
        and controls.txt_subtotal.value
    ):
        try:

            datetime.strptime(
                controls.txt_fecha.value,
                "%d-%m-%Y"
            )

            float(
                controls.txt_subtotal.value.replace(",", "")
            )

            if Factura.existe_compra(
                controls.txt_codigo_generacion.value
            ):

                mostrar_error(
                    page,
                    "Factura duplicada",
                    "Esta compra ya se encuentra registrada."
                )

        except Exception:
            pass


def validar_guardado(state, controls, mostrar_error, page):

    if state.periodo_actual is None:
        mostrar_error(
            page,
            "Validación",
            "Debe seleccionar un período."
        )
        return False

    if not controls.txt_fecha.value:

        mostrar_error(
            page,
            "Validación",
            "Debe ingresar una fecha."
        )

        return False

    try:

        datetime.strptime(
            controls.txt_fecha.value,
            "%d-%m-%Y"
        )

    except ValueError:

        mostrar_error(
            page,
            "Validación",
            "La fecha debe tener el formato dd-mm-yyyy."
        )

        return False

    if not validar_codigo_generacion(
        controls,
        lambda titulo, mensaje: mostrar_error(
            page,
            titulo,
            mensaje,
        ),
    ):
        return False


    if not validar_subtotal(
        controls,
        lambda titulo, mensaje: mostrar_error(
            page,
            titulo,
            mensaje,
        ),
    ):
        return False
    
    if not controls.dd_tipo_documento.value:

        mostrar_error(
            page,
            "Validación",
            "Debe seleccionar un tipo de documento."
        )

        return False

    if not controls.dd_emisor.value:

        mostrar_error(
            page,
            "Validación",
            "Debe seleccionar un emisor."
        )

        return False

    if not controls.dd_clase_documento.value:

        mostrar_error(
            page,
            "Validación",
            "Debe seleccionar una clase de documento."
        )

        return False

    return True


def validar_dropdown(control, mensaje, mostrar_error, page):

    if not control.value:

        mostrar_error(
            page,
            "Validación",
            mensaje,
        )

        return False

    return True


# ==========================================================
# ALERTA PROFESIONAL
# ==========================================================

def mostrar_error(*args):
    """
    Permite utilizar:

        mostrar_error(page, titulo, mensaje)

    o

        mostrar_error(titulo, mensaje)

    """

    # ---------------------------------

    if len(args) == 2:
        titulo, mensaje = args
        page = None

    elif len(args) == 3:
        page, titulo, mensaje = args

    else:
        raise TypeError(
            "mostrar_error() recibe "
            "(titulo, mensaje) "
            "o "
            "(page, titulo, mensaje)"
        )

    # ---------------------------------

    if page is None:

        print(f"{titulo}: {mensaje}")

        return

    # ---------------------------------

    dialog = ft.AlertDialog(

        modal=True,

        title=ft.Row(
            [
                ft.Icon(
                    ft.Icons.ERROR_OUTLINE,
                    color=ft.Colors.RED_600,
                    size=28,
                ),

                ft.Text(
                    titulo,
                    weight=ft.FontWeight.BOLD,
                    size=18,
                ),
            ]
        ),

        content=ft.Container(

            width=320,

            padding=20,

            content=ft.Text(
                mensaje,
                size=15,
            ),
        ),

        actions=[
            ft.FilledButton(
                "Aceptar"
            )
        ],

        actions_alignment=ft.MainAxisAlignment.END,
    )

    def cerrar(e):
        dialog.open = False
        page.update()

    dialog.actions[0].on_click = cerrar

    page.show_dialog(dialog)

def mostrar_exito(page, titulo, mensaje):

    dialog = ft.AlertDialog(

        modal=True,

        title=ft.Row(
            [
                ft.Icon(
                    ft.Icons.CHECK_CIRCLE_OUTLINE,
                    color=ft.Colors.GREEN_600,
                    size=28,
                ),

                ft.Text(
                    titulo,
                    weight=ft.FontWeight.BOLD,
                    size=18,
                ),
            ]
        ),

        content=ft.Container(

            width=320,

            padding=20,

            content=ft.Text(
                mensaje,
                size=15,
            ),
        ),

        actions=[
            ft.FilledButton(
                "Aceptar"
            )
        ],

        actions_alignment=ft.MainAxisAlignment.END,
    )

    def cerrar(e):
        dialog.open = False
        page.update()

    dialog.actions[0].on_click = cerrar

    page.show_dialog(dialog)