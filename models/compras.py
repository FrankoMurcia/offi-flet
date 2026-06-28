from database.conexion import conectar

class Factura:

    @staticmethod
    def existe_compra(codigo_generacion):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM compra
            WHERE codigo_generacion =?
        """, (codigo_generacion,))

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

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO compra(fecha, codigo_generacion, numero_control, sello_recepcion, subtotal, iva, iva_percibido, total, id_tipo_documento, id_emisor, id_clase_documento, clasificacion, sector, tipo_costo_gasto, tipo_operacion, id_periodo,
            compras_internas_exentas,
            internaciones_exentas_no_sujetas,
            importaciones_exentas_no_sujetas,
            internaciones_gravadas_bienes,
            importaciones_gravadas_bienes,
            importaciones_gravadas_servicios)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,(fecha, codigo_generacion, numero_control, sello_recepcion, subtotal, iva, iva_percibido,total, id_tipo_documento, id_emisor, id_clase_documento, clasificacion, sector, tipo_costo_gasto, tipo_operacion, id_periodo,
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

        cursor.execute("SELECT * FROM compra")

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

            id_compra
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id_compra):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM compra WHERE id=?",
            (id_compra,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def obtener_por_periodo(id_periodo):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM compra
            WHERE id_periodo=?
            ORDER BY fecha DESC
        """, (id_periodo,))

        datos = cursor.fetchall()

        conn.close()

        return datos
