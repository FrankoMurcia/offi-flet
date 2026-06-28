from views.compras.exportaciones import exportar_csv, exportar_excel

# Exportaciones
def descargar_csv(page, state, mostrar_mensaje, mostrar_error):

    archivo = exportar_csv(
        state.periodo_actual
    )

    if archivo:

        mostrar_mensaje(
            page,
            f"Archivo guardado en\n{archivo}"
        )

    else:

        mostrar_error(
            page,
            "Error",
            "No existen compras."
        )

def descargar_excel(page, state, mostrar_mensaje, mostrar_error):

    archivo = exportar_excel(
        state.periodo_actual
    )

    if archivo:

        mostrar_mensaje(
            page,
            f"Archivo guardado en\n{archivo}"
        )

    else:

        mostrar_error(
            page,
            "Error",
            "No existen compras."
        )