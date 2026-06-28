import csv
import os
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter

from models.compras import Factura
from models.emisor import Emisor
from models.Clasificaciones.tipo_documento import TipoDocumento

from datetime import datetime

def _obtener_datos(periodo_actual):

    if not periodo_actual:
        return []

    return Factura.obtener_por_periodo(periodo_actual)

def exportar_csv(periodo_actual):

    nombre = datetime.now().strftime("compras_%Y%m%d_%H%M%S.csv")
    datos = _obtener_datos(periodo_actual)

    if not datos:
        return False
    
    ruta = Path("exports/csv")

    ruta.mkdir(
        parents=True,
        exist_ok=True
    )

    archivo = ruta / nombre

    with open(
        archivo,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Tipo Documento",
            "Fecha",
            "Código Generación",
            "Numero de Control",
            "Sello Recepción",
            "Proveedor",
            "Subtotal",
            "IVA",
            "Total"
        ])

        for f in datos:

            writer.writerow([

                TipoDocumento.obtener_por_id(f[15]),

                f[1],

                f[2],

                f[3],

                f[4],

                Emisor.obtener_por_id(f[16]),

                f[5],

                f[6],

                f[7]
            ])
    os.startfile(archivo)
    return archivo

def exportar_excel(periodo_actual):

    nombre = datetime.now().strftime("compras_%Y%m%d_%H%M%S.xlsx")
    datos = _obtener_datos(periodo_actual)

    if not datos:
        return False

    ruta = Path("exports/compras")
    ruta.mkdir(parents=True, exist_ok=True)

    archivo = ruta / nombre

    wb = Workbook()
    ws = wb.active
    ws.title = "Compras"

    from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
    from openpyxl.utils import get_column_letter

    # =====================================================
    # ESTILOS
    # =====================================================

    color_principal = "2F5597"
    color_encabezado = "EDEDED"
    color_borde = "D9D9D9"
    color_fila = "FAFAFA"

    borde = Border(
        left=Side(style="thin", color=color_borde),
        right=Side(style="thin", color=color_borde),
        top=Side(style="thin", color=color_borde),
        bottom=Side(style="thin", color=color_borde),
    )

    fuente_titulo = Font(
        name="Calibri",
        size=18,
        bold=True,
        color=color_principal
    )

    fuente_subtitulo = Font(
        name="Calibri",
        size=10,
        color="666666"
    )

    fuente_encabezado = Font(
        name="Calibri",
        size=11,
        bold=True,
        color="000000"
    )

    fuente_normal = Font(
        name="Calibri",
        size=11
    )

    fuente_total = Font(
        name="Calibri",
        size=11,
        bold=True
    )

    relleno_encabezado = PatternFill(
        "solid",
        fgColor=color_encabezado
    )

    relleno_alterno = PatternFill(
        "solid",
        fgColor=color_fila
    )

    # =====================================================
    # TITULO
    # =====================================================

    ws.merge_cells("A1:I1")

    c = ws["A1"]
    c.value = "REPORTE DE COMPRAS"
    c.font = fuente_titulo

    ws["A2"] = "Período"
    ws["B2"] = str(periodo_actual)

    ws["G2"] = "Generado"

    ws["H2"] = datetime.now().strftime("%d/%m/%Y %H:%M")

    ws["A2"].font = fuente_subtitulo
    ws["B2"].font = fuente_subtitulo
    ws["G2"].font = fuente_subtitulo
    ws["H2"].font = fuente_subtitulo

    # =====================================================
    # ENCABEZADOS
    # =====================================================

    encabezados = [
        "Tipo Documento",
        "Fecha",
        "Código Generación",
        "Número Control",
        "Sello Recepción",
        "Proveedor",
        "Subtotal",
        "IVA",
        "Total"
    ]

    fila_inicio = 4

    for col, texto in enumerate(encabezados, start=1):

        celda = ws.cell(fila_inicio, col)

        celda.value = texto
        celda.font = fuente_encabezado
        celda.fill = relleno_encabezado
        celda.alignment = Alignment(horizontal="center", vertical="center")
        celda.border = borde

    # =====================================================
    # DATOS
    # =====================================================

    fila = fila_inicio + 1

    for factura in datos:

        valores = [

            TipoDocumento.obtener_por_id(factura[15]),
            str(factura[1]),
            str(factura[2]),
            str(factura[3]),
            str(factura[4]),
            Emisor.obtener_por_id(factura[16]),
            float(factura[5]),
            float(factura[6]),
            float(factura[7])

        ]

        for col, valor in enumerate(valores, start=1):

            celda = ws.cell(fila, col)

            celda.value = valor
            celda.font = fuente_normal
            celda.border = borde

            if fila % 2 == 0:
                celda.fill = relleno_alterno

            if col == 2:
                celda.alignment = Alignment(horizontal="center")

            elif col >= 7:
                celda.alignment = Alignment(horizontal="right")
                celda.number_format = '$ #,##0.00'

            else:
                celda.alignment = Alignment(horizontal="left")

        fila += 1

    # =====================================================
    # TOTAL
    # =====================================================

    ws.cell(fila + 1, 8).value = "TOTAL"

    ws.cell(fila + 1, 8).font = fuente_total

    ws.cell(fila + 1, 8).alignment = Alignment(horizontal="right")

    ws.cell(fila + 1, 9).value = f"=SUM(I5:I{fila-1})"

    ws.cell(fila + 1, 9).font = fuente_total

    ws.cell(fila + 1, 9).number_format = '$ #,##0.00'

    ws.cell(fila + 1, 8).border = borde
    ws.cell(fila + 1, 9).border = borde

    # =====================================================
    # AUTOAJUSTAR COLUMNAS
    # =====================================================

    for columna in ws.columns:

        longitud = 0

        letra = get_column_letter(columna[0].column)

        for celda in columna:

            if celda.coordinate in ws.merged_cells:
                continue

            if celda.value:

                longitud = max(longitud, len(str(celda.value)))

        ws.column_dimensions[letra].width = min(longitud + 4, 45)

    # =====================================================
    # CONFIGURACIÓN
    # =====================================================

    ws.freeze_panes = "A5"

    ws.auto_filter.ref = f"A4:I{fila-1}"

    ws.sheet_view.showGridLines = False

    ws.row_dimensions[1].height = 28
    ws.row_dimensions[4].height = 24

    wb.save(archivo)

    os.startfile(archivo)

    return archivo
