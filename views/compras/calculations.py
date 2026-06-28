from models.emisor import Emisor
from views.compras.controls import ComprasControls

def calcular_totales(page, controls):
        try:
            subtotal = float(controls.txt_subtotal.value.replace(",", ""))

            iva = subtotal * 0.13
            iva_percibido = 0

            if (
                controls.dd_emisor.value
                and Emisor.obtener_tamaño_por_id(int(controls.dd_emisor.value)) == 3
                and subtotal >= 100
            ):
                iva_percibido = subtotal * 0.01

            iva = round(iva,2)
            iva_percibido = round(iva_percibido,2)
            total = round(subtotal + iva + iva_percibido, 2)

            controls.txt_iva.value = f"{iva:,.2f}"
            controls.txt_iva_percibido.value =(f"{iva_percibido:,.2f}") 
            controls.txt_total.value = f"{total:,.2f}"

        except ValueError:
            controls.txt_iva.value = ""
            controls.txt_total.value = ""
        page.update()