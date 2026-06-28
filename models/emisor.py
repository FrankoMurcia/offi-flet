from database.conexion import conectar

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

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO emisor(nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica, telefono, correo_electronico, direccion)
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """,(nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica,telefono, correo_electronico, direccion))

        conn.commit()
        conn.close()
    
    @staticmethod
    def  obtener_todos():

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM emisor")

        datos = cursor.fetchall()

        conn.close()

        return datos
    
    @staticmethod
    def buscar_por_nit(nit):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM emisor
            WHERE nit LIKE ?
            ORDER BY nombre_comercial
        """, (f"{nit}%",))

        datos = cursor.fetchall()

        conn.close()

        return datos
    
    @staticmethod
    def obtener_por_id(id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT nombre_comercial FROM emisor WHERE id=?",
            (id_emisor,)
        )

        dato = cursor.fetchone()

        conn.close()

        return dato[0] if dato else "No encontrado"

    @staticmethod
    def editar(id_emisor,nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica, telefono, correo_electronico, direccion):

        conn = conectar()
        cursor = conn.cursor()

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
        """,(nombre_comercial, razon_social, nit, dui, nrc, tamaño_contribuyente, actividad_economica, telefono, correo_electronico, direccion, id_emisor)) 

        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM emisor WHERE id=?",
            (id_emisor,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def existe_nit(nit):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM emisor WHERE nit = ?",
            (nit,)
        )

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def existe_nit_otro(nit, id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM emisor
            WHERE nit = ?
            AND id <> ?
        """, (nit, id_emisor))

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def existe_nrc(nrc):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM emisor WHERE nrc = ?",
            (nrc,)
        )

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def existe_nrc_otro(nrc, id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM emisor
            WHERE nrc = ?
            AND id <> ?
        """, (nrc, id_emisor))

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def obtener_tamaño_por_id(id_emisor):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT tamaño_contribuyente
            FROM emisor
            WHERE id = ?
        """, (id_emisor,))

        dato = cursor.fetchone()

        conn.close()

        return dato[0] if dato else None