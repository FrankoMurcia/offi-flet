from views.compras.modal_controller import abrir_modal


def crear_callback_modal(
    page,
    state,
    controls,
    limpiar,
    abrir_proveedor,
    btn_clasificacion,
    btn_fecha,
    sugerencias,
    get_cargar,
):

    return lambda factura=None: abrir_modal(
        page=page,
        state=state,
        controls=controls,
        factura=factura,
        limpiar=limpiar,
        cargar=get_cargar(),
        abrir_proveedor=abrir_proveedor,
        btn_clasificacion=btn_clasificacion,
        btn_fecha=btn_fecha,
        sugerencias=sugerencias,
    )