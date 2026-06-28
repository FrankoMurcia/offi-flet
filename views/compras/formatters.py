import re

#formateador de fecha
def formatear_fecha(e, txt_fecha, page):
        valor = re.sub(r"\D", "", e.control.value)
        if len(valor) > 8:
            valor = valor[:8]
        resultado = ""

        if len(valor) >= 2:
            resultado += valor[:2]
        else:
            resultado += valor

        if len(valor) > 2:
            resultado += "-" + valor[2:4]

        if len(valor) > 4:
            resultado += "-" + valor[4:8]

        txt_fecha.value = resultado
        page.update()


#Formateador del codigo de generacion
def formatear_codigo_generacion(e, txt_codigo_generacion, page):
        valor = e.control.value.upper()

        #Solo letras y numeros
        valor = re.sub(r"[^A-Z0-9]", "", valor)

        #Maximo 32 caracteres
        valor = valor[:32]

        resultado = ""

        grupos = [8,4,4,4,12]
        posicion = 0

        for grupo in grupos:
            if len(valor) > posicion:
                if resultado:
                    resultado += "-"
                resultado += valor[posicion:posicion + grupo]
            posicion += grupo
        txt_codigo_generacion.value = resultado
        page.update()

#Formateador de numero de control
def formatear_numero_control(e, txt_numero_control, page):
        valor = e.control.value.upper()

        #Solo letras y numeros
        valor = re.sub(r"[^A-Z0-9]", "", valor)

        #Maximo 28 caracteres reales (sin guiones)
        valor = valor[:28]

        resultado = ""

        if len(valor) > 0:
            resultado += valor[:3] #DTE
        if len(valor) > 3:
            resultado += "-" + valor[3:5] # Tipo de documento
        if len(valor) >5:
            resultado += "-" + valor[5:13] # Tipo de establecimiento y Punto de venta
        if len(valor) > 13:
            resultado += "-" + valor[13:28] #Numero de correlativo

        txt_numero_control.value = resultado
        page.update()

#Formateador de sello de recepcion
def formatear_sello_recepcion(e, txt_sello_recepcion, page):

        valor= e.control.value.upper()

        #Solo letras y numeros
        valor = re.sub(r"[^A-Z0-9]", "", valor)

        #Maximo 40 caracteres
        valor = valor[:40]

        txt_sello_recepcion.value = valor
        page.update()

#Formateador de subtotal
def formatear_subtotal(e, txt_subtotal, page):

        try:
            valor = float(
                txt_subtotal.value.replace(",", "")
            )

            txt_subtotal.value = f"{valor:,.2f}"

        except ValueError:
            pass

        page.update()