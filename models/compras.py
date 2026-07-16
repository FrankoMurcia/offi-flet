from database.conexion import conectar
from auth import session

class Factura:

    @staticmethod
    def existe_compra(codigo_generacion):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        SELECT COUNT(*)
        FROM compra
        WHERE codigo_generacion=?
        AND id_usuario=?
        """, (
            codigo_generacion,
            id_usuario
        ))

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe

    @staticmethod
    def guardar(fecha, codigo_generacion, numero_control, sello_recepcion, subtotal, iva,iva_percibido, total,id_tipo_documento, id_emisor, id_clase_documento, clasificacion, sector, tipo_costo_gasto, tipo_operacion, id_periodo,
                compras_internas_exentas,
                internaciones_exentas_no_sujetas,
                importaciones_exentas_no_sujetas,
                internaciones_gravadas_bienes,
                importaciones_gravadas_bienes,
                importaciones_gravadas_servicios, ):

        id_usuario = session.id()

        if id_usuario is None:
            raise Exception("No existe un usuario autenticado.")

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO compra(id_usuario, fecha, codigo_generacion, numero_control, sello_recepcion, subtotal, iva, iva_percibido, total, id_tipo_documento, id_emisor, id_clase_documento, clasificacion, sector, tipo_costo_gasto, tipo_operacion, id_periodo,
            compras_internas_exentas,
            internaciones_exentas_no_sujetas,
            importaciones_exentas_no_sujetas,
            internaciones_gravadas_bienes,
            importaciones_gravadas_bienes,
            importaciones_gravadas_servicios)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,(id_usuario, fecha, codigo_generacion, numero_control, sello_recepcion, subtotal, iva, iva_percibido,total, id_tipo_documento, id_emisor, id_clase_documento, clasificacion, sector, tipo_costo_gasto, tipo_operacion, id_periodo,
            compras_internas_exentas,
            internaciones_exentas_no_sujetas,
            importaciones_exentas_no_sujetas,
            internaciones_gravadas_bienes,
            importaciones_gravadas_bienes,
            importaciones_gravadas_servicios,))

        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        SELECT *
        FROM compra
        WHERE id_usuario=?
        ORDER BY fecha DESC
        """, (id_usuario,))

        datos = cursor.fetchall()

        conn.close()

        return datos

    @staticmethod
    def editar(
        id_compra,
        fecha,
        codigo_generacion,
        numero_control,
        sello_recepcion,
        subtotal,
        iva,
        iva_percibido,
        total,
        compras_internas_exentas,
        internaciones_exentas_no_sujetas,
        importaciones_exentas_no_sujetas,
        internaciones_gravadas_bienes,
        importaciones_gravadas_bienes,
        importaciones_gravadas_servicios,
        id_tipo_documento,
        id_emisor,
        id_clase_documento,
        clasificacion,
        sector,
        tipo_costo_gasto,
        tipo_operacion,
        id_periodo
    ):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        UPDATE compra
        SET fecha=?,
            codigo_generacion=?,
            numero_control=?,
            sello_recepcion=?,
            subtotal=?,
            iva=?,
            iva_percibido=?,
            total=?,

            compras_internas_exentas=?,
            internaciones_exentas_no_sujetas=?,
            importaciones_exentas_no_sujetas=?,
            internaciones_gravadas_bienes=?,
            importaciones_gravadas_bienes=?,
            importaciones_gravadas_servicios=?,

            id_tipo_documento=?,
            id_emisor=?,
            id_clase_documento=?,
            clasificacion=?,
            sector=?,
            tipo_costo_gasto=?,
            tipo_operacion=?,
            id_periodo=?

        WHERE id=?
        AND id_usuario=?
        """, (
            fecha,
            codigo_generacion,
            numero_control,
            sello_recepcion,
            subtotal,
            iva,
            iva_percibido,
            total,

            compras_internas_exentas,
            internaciones_exentas_no_sujetas,
            importaciones_exentas_no_sujetas,
            internaciones_gravadas_bienes,
            importaciones_gravadas_bienes,
            importaciones_gravadas_servicios,

            id_tipo_documento,
            id_emisor,
            id_clase_documento,
            clasificacion,
            sector,
            tipo_costo_gasto,
            tipo_operacion,
            id_periodo,

            id_compra,
            id_usuario
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id_compra):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        DELETE FROM compra
        WHERE id=?
        AND id_usuario=?
        """,
        (
            id_compra,
            id_usuario
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def obtener_por_periodo(id_periodo):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        SELECT *
        FROM compra
        WHERE id_periodo=?
        AND id_usuario=?
        ORDER BY fecha DESC
        """, (
            id_periodo,
            id_usuario
        ))

        datos = cursor.fetchall()

        conn.close()

        return datos
