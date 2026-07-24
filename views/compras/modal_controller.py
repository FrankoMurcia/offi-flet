from datetime import datetime
import asyncio

import flet as ft

from models.emisor import Emisor
from models.Clasificaciones.clasificacion import Clasificacion
from models.Clasificaciones.sector import Sector
from models.Clasificaciones.tipo_costo_gasto import TipoCostoGasto
from models.Clasificaciones.tipo_operacion import TipoOperacion
from views.compras.clasificacion_service import actualizar_textos

from views.compras.dialogs import (
    mostrar_confirmacion,
)

from views.compras.validaciones import (
    mostrar_error,
    mostrar_exito,
)


from views.compras.validaciones import (
    validar_guardado,
)

from views.compras.compras_service import (
    guardar_compra,
    compra_duplicada,
)

from views.compras.formulario import crear_modal

def abrir_modal(page, state, controls, factura, limpiar, cargar, abrir_proveedor, btn_clasificacion, btn_fecha, sugerencias,):

        if state.periodo_actual is None:
            mostrar_error(
                page,
                "Período requerido",
                "Debe seleccionar un período."
            )
            return

        if factura:

            state.id_edicion = factura[0]

            controls.txt_fecha.value = datetime.strptime(
                str(factura[2]),
                "%Y-%m-%d"
            ).strftime("%d-%m-%Y")

            controls.txt_codigo_generacion.value = factura[3]
            controls.txt_numero_control.value = factura[4]
            controls.txt_sello_recepcion.value = factura[5]

            controls.txt_subtotal.value = str(factura[6])
            controls.txt_iva.value = str(factura[7])
            controls.txt_total.value = str(factura[8])
            controls.txt_iva_percibido.value = str(factura[9])

            controls.txt_compras_internas_exentas.value = str(factura[10])
            controls.txt_internaciones_exentas_no_sujetas.value = str(factura[11])
            controls.txt_importaciones_exentas_no_sujetas.value = str(factura[12])

            controls.txt_internaciones_gravadas_bienes.value = str(factura[13])
            controls.txt_importaciones_gravadas_bienes.value = str(factura[14])
            controls.txt_importaciones_gravadas_servicios.value = str(factura[15])

            controls.dd_tipo_documento.value = str(factura[16])
            controls.dd_emisor.value = str(factura[17])

            nombre_emisor = Emisor.obtener_por_id(factura[17])
            controls.txt_nombre_emisor.value = nombre_emisor

            controls.dd_clase_documento.value = str(factura[18])

            state.clasificacion_seleccionada = factura[19]
            state.sector_seleccionado = factura[20]
            state.tipo_costo_gasto_seleccionado = factura[21]
            state.tipo_operacion_seleccionado = factura[22]

            actualizar_textos(state, controls)

            titulo = "Editar Compra"

        else:

            state.id_edicion = None
            limpiar()

            state.clasificacion_seleccionada = None
            state.sector_seleccionado = None
            state.tipo_costo_gasto_seleccionado = None
            state.tipo_operacion_seleccionado = None
            actualizar_textos(state,controls)

            titulo = "Nueva Compra"


        def guardar_modal(e):


            def ejecutar_guardado():
                try:

                    if compra_duplicada(state, controls):
                        mostrar_error(
                            page,
                            "Factura duplicada",
                            "Ya existe una compra."
                        )
                        return

                    guardado = guardar_compra(state, controls, mostrar_error, page)

                    if not guardado:
                        return False

                    print("1")
                    cerrar_modal(dialog)
                    page.update()

                    print("2")
                    limpiar()

                    print("3")
                    cargar()

                    print("4")
                    page.update()

                    print("5")

                    async def mostrar_exito_despues():

                        await asyncio.sleep(0.3)

                        if state.id_edicion is None:

                            mostrar_exito(
                                page,
                                "Éxito",
                                "Compra guardada correctamente."
                            )

                        else:

                            mostrar_exito(
                                page,
                                "Éxito",
                                "Compra actualizada correctamente."
                            )


                    page.run_task(
                        mostrar_exito_despues
                    )

                    return True

                except Exception as ex:
                    print(ex)
                    raise

            if not validar_guardado(state, controls, mostrar_error, page
            ):
                return

            mostrar_confirmacion(
                page,
                "Confirmación",
                "¿Desea guardar los cambios?",
                ejecutar_guardado
            )

        def ir_a_proveedores(e):
            if dialog is not None:
                dialog.open = False
            if getattr(page, "dialog", None) is dialog:
                page.dialog = None
            page.update()

            limpiar()

            abrir_proveedor()

        controls.btn_nuevo_proveedor = ft.ElevatedButton(
            "Proveedor no encontrado",
            icon=ft.Icons.ADD,
            visible=False,
            on_click=ir_a_proveedores  # o tu método de navegación
        )

        def cerrar_modal(dialog):

            print("Entro a cerrar_modal")

            if dialog is not None:
                dialog.open = False

            if getattr(page, "dialog", None) is dialog:
                page.dialog = None

            page.update()
            print("Salio de cerrar_modal")

        dialog = crear_modal(
            titulo=titulo,
            controls=controls,
            sugerencias=sugerencias,
            btn_nuevo_proveedor=controls.btn_nuevo_proveedor,
            btn_clasificacion=btn_clasificacion,
            btn_fecha=btn_fecha,
            guardar_modal=guardar_modal,
            cerrar_modal=cerrar_modal,
        )
        print("ID crear_modal:", id(dialog))

        page.show_dialog(dialog)
        page.update()