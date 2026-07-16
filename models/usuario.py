from database.conexion import conectar
from auth.password import (
    encriptar,
    verificar
)

class Usuario:

    @staticmethod
    def guardar(usuario, contraseña, nombre, rol):

        conn = conectar()
        cursor = conn.cursor()
        
        hash_password = encriptar(contraseña)

        cursor.execute("""
        INSERT INTO usuario(
            usuario,
            contraseña,
            nombre,
            rol
        )
        VALUES(?,?,?,?)
        """,
        (
            usuario,
            hash_password,
            nombre,
            rol
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM usuario
        ORDER BY nombre
        """)

        datos = cursor.fetchall()

        conn.close()

        return datos
    
    @staticmethod
    def obtener_por_id(id_usuario):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM usuario
        WHERE id=?
        """,
        (id_usuario,)
        )

        dato = cursor.fetchone()

        conn.close()

        return dato
    
    @staticmethod
    def eliminar(id_usuario):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE
        FROM usuario
        WHERE id=?
        """,
        (id_usuario,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def editar(
        id_usuario,
        usuario,
        contraseña,
        nombre,
        rol
    ):

        conn = conectar()
        cursor = conn.cursor()

        hash_password = encriptar(contraseña)

        cursor.execute("""
        UPDATE usuario
        SET

            usuario=?,
            contraseña=?,
            nombre=?,
            rol=?

        WHERE id=?
        """,
        (
            usuario,
            hash_password,
            nombre,
            rol,
            id_usuario
        ))

        conn.commit()
        conn.close()
    
    @staticmethod
    def existe_usuario(usuario):

        conn = conectar()

        cursor = conn.cursor()

        cursor.execute("""

        SELECT COUNT(*)

        FROM usuario

        WHERE usuario=?

        """,(usuario,))

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def existe_usuario_otro(usuario,id_usuario):

        conn = conectar()

        cursor = conn.cursor()

        cursor.execute("""

        SELECT COUNT(*)

        FROM usuario

        WHERE usuario=?

        AND id<>?

        """,(usuario,id_usuario))

        existe = cursor.fetchone()[0] > 0

        conn.close()

        return existe
    
    @staticmethod
    def autenticar(usuario, contraseña):

        conn = conectar()

        cursor = conn.cursor()
        
        import hashlib

        contraseña = hashlib.sha256(
            contraseña.encode()
        ).hexdigest()

        cursor.execute("""
            SELECT *
            FROM usuario
            WHERE usuario=?
            AND contraseña=?
        """,
        (
            usuario,
            contraseña
        ))

        datos = cursor.fetchone()

        conn.close()

        return datos