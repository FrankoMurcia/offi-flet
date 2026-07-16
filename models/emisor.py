from database.conexion import conectar
from auth import session

class Emisor:

    TAMAÑO_CONTRIBUYENTE = {
        1: "Pequeño",
        2: "Mediano",
        3: "Grande",
        4: "Fiscalización o Agente de Percepción",
        5: "Retención No Inscritos al IVA 13%"
    }        

    @classmethod
    def obtener_tamaño_contribuyente(cls, id_tamaño):
        return cls.TAMAÑO_CONTRIBUYENTE.get(
            id_tamaño,
            "No definido"
        )

    @staticmethod
    def guardar(nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica, telefono, correo_electronico, direccion):
        
        id_usuario = session.id()

        if id_usuario is None:
            raise Exception("No existe un usuario autenticado.")
        
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO emisor(id_usuario, nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica, telefono, correo_electronico, direccion)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """,(id_usuario, nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica,telefono, correo_electronico, direccion))

        conn.commit()
        conn.close()
    
    @staticmethod
    def  obtener_todos():

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        SELECT *
        FROM emisor
        WHERE id_usuario=?
        ORDER BY nombre_comercial
        """,
        (id_usuario,))

        datos = cursor.fetchall()

        conn.close()

        return datos
    
    @staticmethod
    def buscar_por_nit(nit):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        SELECT *
        FROM emisor
        WHERE nit LIKE ?
        AND id_usuario=?
        ORDER BY nombre_comercial
        """,
        (
            f"{nit}%",
            id_usuario
        ))

        datos = cursor.fetchall()

        conn.close()

        return datos
    
    @staticmethod
    def obtener_por_id(id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        SELECT nombre_comercial
        FROM emisor
        WHERE id=?
        AND id_usuario=?
        """,
        (
            id_emisor,
            id_usuario
        ))

        dato = cursor.fetchone()

        conn.close()

        return dato[0] if dato else "No encontrado"

    @staticmethod
    def editar(id_emisor,nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica, telefono, correo_electronico, direccion):

        conn = conectar()
        cursor = conn.cursor()
        id_usuario = session.id()

        cursor.execute("""
        UPDATE emisor
        SET nombre_comercial=?,
            razon_social=?, 
            nit=?, 
            dui=?, 
            nrc=?,
            tamaño_contribuyente=?,
            actividad_economica=?, 
            telefono=?, 
            correo_electronico=?, 
            direccion=?
        WHERE id=?
        AND id_usuario=?
        """,(nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica, telefono, correo_electronico, direccion, id_emisor, id_usuario)) 

        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        DELETE
        FROM emisor
        WHERE id=?
        AND id_usuario=?
        """,
        (
            id_emisor,
            id_usuario
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def existe_nit(nit):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
        SELECT COUNT(*)
        FROM emisor
        WHERE nit=?
        AND id_usuario=?
        """,
        (
            nit,
            id_usuario
        ))

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def existe_nit_otro(nit, id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
            SELECT COUNT(*)
            FROM emisor
            WHERE nit = ?
            AND id <> ?
            AND id_usuario=?
        """, (nit, id_emisor, id_usuario))

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def existe_nrc(nrc):

        conn = conectar()
        cursor = conn.cursor()
        id_usuario= session.id()
        cursor.execute(
            "SELECT COUNT(*) FROM emisor WHERE nrc = ? AND id_usuario=?",
            (nrc,id_usuario)
        )

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def existe_nrc_otro(nrc, id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
            SELECT COUNT(*)
            FROM emisor
            WHERE nrc = ?
            AND id <> ?
            AND id_usuario=?
        """, (nrc, id_emisor, id_usuario))

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def obtener_tamaño_por_id(id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()

        cursor.execute("""
            SELECT tamaño_contribuyente
            FROM emisor
            WHERE id = ?
            AND id_usuario=?
        """, (id_emisor,id_usuario))

        dato = cursor.fetchone()

        conn.close()

        return dato[0] if dato else None

    @staticmethod
    def obtener_datos_por_id(id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        id_usuario = session.id()
        
        cursor.execute("""
            SELECT *
            FROM emisor
            WHERE id = ?
            AND id_usuario=?
        """, (id_emisor,id_usuario))

        dato = cursor.fetchone()

        conn.close()

        return dato