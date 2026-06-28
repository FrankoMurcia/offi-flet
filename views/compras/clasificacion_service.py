from models.Clasificaciones.clasificacion import Clasificacion
from models.Clasificaciones.sector import Sector
from models.Clasificaciones.tipo_costo_gasto import TipoCostoGasto
from models.Clasificaciones.tipo_operacion import TipoOperacion


def actualizar_textos(state, controls):

    descripcion = Clasificacion.obtener_por_id(
        state.clasificacion_seleccionada
    )

    controls.txt_clasificacion.value = (
        f"{state.clasificacion_seleccionada}. {descripcion}"
        if state.clasificacion_seleccionada
        else "Sin seleccionar"
    )

    descripcion = Sector.obtener_por_id(
        state.sector_seleccionado
    )

    controls.txt_sector.value = (
        f"{state.sector_seleccionado}. {descripcion}"
        if state.sector_seleccionado
        else "Sin seleccionar"
    )

    descripcion = TipoCostoGasto.obtener_por_id(
        state.tipo_costo_gasto_seleccionado
    )

    controls.txt_tipo_gasto.value = (
        f"{state.tipo_costo_gasto_seleccionado}. {descripcion}"
        if state.tipo_costo_gasto_seleccionado
        else "Sin seleccionar"
    )
    
    descripcion = TipoOperacion.obtener_por_id(
        state.tipo_operacion_seleccionado
    )

    controls.txt_tipo_operacion.value = (
        f"{state.tipo_operacion_seleccionado}. {descripcion}"
        if state.tipo_operacion_seleccionado
        else "Sin seleccionar"
    )
