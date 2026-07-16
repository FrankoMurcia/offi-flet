from database.conexion import conectar
from auth import session


class Periodo:

    @staticmethod
    def guardar(nombre, anio):

        id_usuario = session.id()

        if id_usuario is None:
            raise Exception("No existe un usuario autenticado.")

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO periodo(id_usuario, nombre, anio)
            VALUES(?,?,?)
        """, (id_usuario, nombre, anio,))

        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
            SELECT *
            FROM periodo
            WHERE id_usuario=?
            ORDER BY id DESC
        """,
        (
            id_usuario,
        ))

        datos = cursor.fetchall()

        conn.close()

        return datos
    
    @staticmethod
    def obtener_por_id(id_periodo):

        id_usuario = session.id()

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM periodo
            WHERE id=?
            AND id_usuario=?
        """, (id_periodo, id_usuario,))

        dato = cursor.fetchone()

        conn.close()

        return dato