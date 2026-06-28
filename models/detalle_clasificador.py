from database.conexion import conectar

class DetalleClasificador:

    @staticmethod
    def guardar(id_tipo_documento,id_clase_documento,id_clasificacion,id_sector,id_tipo_costo_gasto,id_tipo_operacion):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO detalle_clasificador(
            id_tipo_documento,
            id_clase_documento,
            id_clasificacion,
            id_sector,
            id_tipo_costo_gasto,
            id_tipo_operacion
        )
        VALUES(?,?,?,?,?,?)
        """, (id_tipo_documento,id_clase_documento,id_clasificacion,id_sector,id_tipo_costo_gasto,id_tipo_operacion))

        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM detalle_clasificador
        """)

        datos = cursor.fetchall()

        conn.close()

        return datos

    @staticmethod
    def obtener_por_tipo_documento(id_tipo_documento):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM detalle_clasificador WHERE id_tipo_documento = ?
        """, (id_tipo_documento,))

        dato = cursor.fetchone()

        conn.close()

        return dato

    @staticmethod
    def editar(id_detalle,id_tipo_documento,id_clase_documento,id_clasificacion,id_sector,id_tipo_costo_gasto,id_tipo_operacion):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE detalle_clasificador
        SET
            id_tipo_documento=?,
            id_clase_documento=?,
            id_clasificacion=?,
            id_sector=?,
            id_tipo_costo_gasto=?,
            id_tipo_operacion=?
        WHERE id=?
        """, (
            id_tipo_documento,
            id_clase_documento,
            id_clasificacion,
            id_sector,
            id_tipo_costo_gasto,
            id_tipo_operacion,
            id_detalle
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id_detalle):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM detalle_clasificador WHERE id=?",
            (id_detalle,)
        )

        conn.commit()
        conn.close()

@staticmethod
def obtener(id_tipo_documento, id_clase_documento):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id_clasificacion,
            id_sector,
            id_tipo_costo_gasto,
            id_tipo_operacion
        FROM detalle_clasificador
        WHERE id_tipo_documento = ?
          AND id_clase_documento = ?
    """, (
        id_tipo_documento,
        id_clase_documento
    ))

    dato = cursor.fetchone()

    conn.close()

    return dato