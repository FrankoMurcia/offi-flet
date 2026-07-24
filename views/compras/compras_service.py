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


    # ==============================
    # Código de generación
    # ==============================

    codigo_generacion = (
        controls.txt_codigo_generacion.value or ""
    ).strip().upper()

    if not codigo_generacion:
        mostrar_error(
            page,
            "Error",
            "El Código de Generación es obligatorio."
        )
        return
    
    # ==============================
    # Subtotal
    # ==============================

    subtotal_texto = (
        controls.txt_subtotal.value or ""
    ).replace(",", "").strip()

    try:
        subtotal = float(subtotal_texto)
    except ValueError:
        mostrar_error(
            page,
            "Error",
            "El subtotal no es válido."
        )
        return
    
    if state.id_edicion is None:

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
        return True
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
            
            state.clasificacion_seleccionada,
            state.sector_seleccionado,
            state.tipo_costo_gasto_seleccionado,
            state.tipo_operacion_seleccionado,

            state.periodo_actual,
        )
        return True
    
    return False

def compra_duplicada(state, controls):

    return(
        state.id_edicion is None and Factura.existe_compra(
            controls.txt_codigo_generacion.value
        )
    )