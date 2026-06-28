from database.conexion import conectar


class Periodo:

    @staticmethod
    def guardar(nombre, anio):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO periodo(nombre, anio)
            VALUES(?,?)
        """, (nombre, anio,))

        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM periodo
            ORDER BY id DESC
        """)

        datos = cursor.fetchall()

        conn.close()

        return datos
    
    @staticmethod
    def obtener_por_id(id_periodo):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM periodo
            WHERE id=?
        """, (id_periodo,))

        dato = cursor.fetchone()

        conn.close()

        return dato