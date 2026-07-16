import flet as ft
from models.emisor import Emisor
from .dialogos import mostrar_alerta, mostrar_confirmacion, mostrar_mensaje


def guardar_emisor(page, form, id_edicion, dialog_emisor, recargar_callback, limpiar_id_callback):
    nombre_comercial = form.txt_nombre_comercial.value.strip()

    if nombre_comercial == "":
        mostrar_mensaje(page, "Ingrese el nombre comercial.")
        return

    if not form.ddl_tamaño_contribuyente.value:
        mostrar_mensaje(page, "Seleccione el tamaño del contribuyente.")
        return

    if id_edicion is None and Emisor.existe_nit(form.txt_nit.value):
        mostrar_alerta(page, "NIT duplicado",
                        f"Ya existe un emisor registrado con el NIT:\n\n{form.txt_nit.value}")
        return

    if id_edicion is None and Emisor.existe_nrc(form.txt_nrc.value):
        mostrar_alerta(page, "NRC duplicado",
                        f"Ya existe un emisor registrado con el NRC:\n\n{form.txt_nrc.value}")
        return

    def ejecutar_guardado():
        if id_edicion is None:
            if Emisor.existe_nit(form.txt_nit.value):
                mostrar_mensaje(page, f"El NIT {form.txt_nit.value} ya se encuentra registrado")
                return

            Emisor.guardar(
                form.txt_nombre_comercial.value, form.txt_razon_social.value,
                form.txt_nit.value, form.txt_dui.value, form.txt_nrc.value,
                int(form.ddl_tamaño_contribuyente.value), form.txt_actividad.value,
                form.txt_telefono.value, form.txt_correo.value, form.txt_direccion.value
            )
            mostrar_mensaje(page, "Emisor guardado correctamente.")

        else:
            if Emisor.existe_nit_otro(form.txt_nit.value, id_edicion):
                mostrar_mensaje(page, "Ya existe otro emisor con este NIT.")
                return

            if Emisor.existe_nrc_otro(form.txt_nrc.value, id_edicion):
                mostrar_alerta(page, "NRC duplicado",
                                f"Ya existe otro emisor registrado con el NRC:\n\n{form.txt_nrc.value}")
                return

            nit = form.txt_nit.value.strip() or None
            dui = form.txt_dui.value.strip() or None
            nrc = form.txt_nrc.value.strip() or None

            Emisor.editar(
                id_edicion, form.txt_nombre_comercial.value, form.txt_razon_social.value,
                nit, dui, nrc, int(form.ddl_tamaño_contribuyente.value),
                form.txt_actividad.value, form.txt_telefono.value,
                form.txt_correo.value, form.txt_direccion.value
            )
            mostrar_mensaje(page, "Emisor actualizado correctamente.")
            limpiar_id_callback()

        dialog_emisor.open = False
        page.update()
        form.limpiar()
        recargar_callback()

    mensaje = "¿Desea guardar este emisor?" if id_edicion is None else "¿Desea actualizar este emisor?"
    mostrar_confirmacion(page, "Confirmación", mensaje, ejecutar_guardado)


def eliminar_emisor(page, id_emisor, recargar_callback):
    def ejecutar_eliminacion():
        Emisor.eliminar(id_emisor)
        mostrar_mensaje(page, "Emisor eliminado correctamente.")
        recargar_callback()

    mostrar_confirmacion(page, "Eliminar emisor", "¿Desea eliminar este emisor?", ejecutar_eliminacion)