from database.conexion import conectar

def crear_tablas():

    conn = conectar()
    cursor = conn.cursor()

    # Usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        usuario TEXT NOT NULL UNIQUE,

        contraseña TEXT NOT NULL,

        nombre TEXT NOT NULL,

        rol TEXT NOT NULL,

        activo INTEGER NOT NULL DEFAULT 1,

        primer_login INTEGER NOT NULL DEFAULT 1,

        fecha_creacion TEXT,

        ultimo_login TEXT

    )
    """)

    # Emisor
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emisor(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
        id_usuario INTEGER NOT NULL,
                   
        nombre_comercial TEXT,
        razon_social TEXT,
        nit TEXT,
        dui TEXT,
        nrc TEXT,
        tamaño_contribuyente INTEGER,
        actividad_economica TEXT,
        telefono TEXT,
        correo_electronico TEXT,
        direccion TEXT,
        
        UNIQUE(id_usuario, nit),
        UNIQUE(id_usuario, nrc),
                   
        FOREIGN KEY(id_usuario)
            REFERENCES usuario(id)
    )
    """)

    # compras
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compra(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
        id_usuario INTEGER NOT NULL,
                   
        fecha TEXT,
                   
        codigo_generacion TEXT,
        numero_control TEXT,
        sello_recepcion TEXT,
                   
        subtotal REAL,
        iva REAL,
        total REAL,
        iva_percibido REAL,
        
        compras_internas_exentas REAL DEFAULT 0,
        internaciones_exentas_no_sujetas REAL DEFAULT 0,
        importaciones_exentas_no_sujetas REAL DEFAULT 0,
        internaciones_gravadas_bienes REAL DEFAULT 0,
        importaciones_gravadas_bienes REAL DEFAULT 0,
        importaciones_gravadas_servicios REAL DEFAULT 0,
                   
        id_tipo_documento INTEGER,
        id_emisor INTEGER,
        id_clase_documento INTEGER,
        
        clasificacion INTEGER NOT NULL,  
        sector INTEGER NOT NULL,
        tipo_costo_gasto INTEGER NOT NULL,
        tipo_operacion INTEGER NOT NULL,
                   
        id_periodo INTEGER,
                   
        UNIQUE(id_usuario, codigo_generacion)
        
        FOREIGN KEY(id_usuario)
            REFERENCES usuario(id),

        FOREIGN KEY(id_emisor)
            REFERENCES emisor(id),

        FOREIGN KEY(id_periodo)
            REFERENCES periodo(id)   
    )
    """)

    #Periodos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS periodo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
        id_usuario INTEGER NOT NULL,
                   
        nombre TEXT,
        anio INTEGER,
        
        FOREIGN KEY(id_usuario)
            REFERENCES usuario(id)
    )
    """)

    conn.commit()
    conn.close()