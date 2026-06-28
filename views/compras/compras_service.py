from datetime import datetime
from models.compras import Factura
from views.compras.validaciones import validar_guardado
import flet as ft

def guardar_compra(state, controls, mostrar_error, page: ft.Page):
    
    if not validar_guardado(state, controls, mostrar_error, page):
        return
     
    fecha_sql = datetime.strptime(
        controls.txt_fecha.value,
        "%d-%m-%Y"
    ).strftime("%Y-%m-%d")

    subtotal = float(controls.txt_subtotal.value.replace(",", ""))
    
    if state.id_edicion is None:

        print("========== CLASIFICACIÓN ==========")
        print("Clasificación:", state.clasificacion_seleccionada)
        print("Sector:", state.sector_seleccionado)
        print("Tipo Gasto:", state.tipo_costo_gasto_seleccionado)
        print("Tipo Operación:", state.tipo_operacion_seleccionado)
        print("===================================")

        Factura.guardar(
            fecha_sql,
            controls.txt_codigo_generacion.value,
            controls.txt_numero_control.value,
            controls.txt_sello_recepcion.value,
            subtotal,                        
            float(controls.txt_iva.value.replace(",","")),
            float(controls.txt_iva_percibido.value.replace(",","")),
            float(controls.txt_total.value.replace(",","")),
            int(controls.dd_tipo_documento.value),
            int(controls.dd_emisor.value),
            int(controls.dd_clase_documento.value),

            # int(controls.txt_clasificacion.value),
            # int(controls.txt_sector.value),
            # int(controls.txt_tipo_gasto.value),
            # int(controls.txt_tipo_operacion.value),

            state.clasificacion_seleccionada,
            state.sector_seleccionado,
            state.tipo_costo_gasto_seleccionado,
            state.tipo_operacion_seleccionado,
            state.periodo_actual,

            float(controls.txt_compras_internas_exentas.value or 0),
            float(controls.txt_internaciones_exentas_no_sujetas.value or 0),
            float(controls.txt_importaciones_exentas_no_sujetas.value or 0),
            float(controls.txt_internaciones_gravadas_bienes.value or 0),
            float(controls.txt_importaciones_gravadas_bienes.value or 0),
            float(controls.txt_importaciones_gravadas_servicios.value or 0),
        )

    else:

        Factura.editar(
            state.id_edicion,
            fecha_sql,
            controls.txt_codigo_generacion.value,
            controls.txt_numero_control.value,
            controls.txt_sello_recepcion.value,
            float(controls.txt_subtotal.value.replace(",","")),
            float(controls.txt_iva.value.replace(",","")),
            float(controls.txt_iva_percibido.value.replace(",","")),
            float(controls.txt_total.value.replace(",","")),

            float(controls.txt_compras_internas_exentas.value or 0),
            float(controls.txt_internaciones_exentas_no_sujetas.value or 0),
            float(controls.txt_importaciones_exentas_no_sujetas.value or 0),
            float(controls.txt_internaciones_gravadas_bienes.value or 0),
            float(controls.txt_importaciones_gravadas_bienes.value or 0),
            float(controls.txt_importaciones_gravadas_servicios.value or 0),

            int(controls.dd_tipo_documento.value),
            int(controls.dd_emisor.value),
            int(controls.dd_clase_documento.value),

            int(controls.dd_clasificacion.value),
            int(controls.dd_sector.value),
            int(controls.dd_tipo_gasto.value),
            int(controls.dd_tipo_operacion.value),

            state.periodo_actual,
        )

def compra_duplicada(state, controls):

    return(
        state.id_edicion is None and Factura.existe_compra(
            controls.txt_codigo_generacion.value
        )
    )