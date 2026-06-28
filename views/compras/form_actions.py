def limpiar(page,state,controls, sugerencias):

        state.clasificacion_seleccionada = None
        state.sector_seleccionado = None
        state.tipo_costo_gasto_seleccionado = None
        state.tipo_operacion_seleccionado = None

        controls.txt_clasificacion.value = "Sin seleccionar"
        controls.txt_sector.value = "Sin seleccionar"
        controls.txt_tipo_gasto.value = "Sin seleccionar"
        controls.txt_tipo_operacion.value = "Sin seleccionar"

        controls.txt_fecha.value = ""
        controls.txt_codigo_generacion.value = ""
        controls.txt_numero_control.value = ""
        controls.txt_sello_recepcion.value = ""
        controls.txt_subtotal.value = ""
        controls.txt_iva.value = ""
        controls.txt_iva_percibido.value = ""
        controls.txt_total.value = ""

        controls.dd_tipo_documento.value = ""
        controls.dd_emisor.value = ""
        controls.txt_buscar_nit.value = ""
        controls.dd_clase_documento.value = ""
        sugerencias.content.controls.clear()
        sugerencias.visible = False
        controls.txt_nombre_emisor.value = ""

        if controls.btn_nuevo_proveedor:
            controls.btn_nuevo_proveedor.visible = False

        page.update()