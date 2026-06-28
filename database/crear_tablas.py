from database.conexion import conectar

def crear_tablas():

    conn = conectar()
    cursor = conn.cursor()

    # Emisor
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emisor(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_comercial TEXT,
        razon_social TEXT,
        nit INTEGER UNIQUE,
        dui INTEGER,
        nrc INTEGER,
        tamaño_contribuyente INTEGER,
        actividad_economica TEXT,
        telefono TEXT,
        correo_electronico TEXT,
        direccion TEXT
    )
    """)

    # Producto
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS producto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        cantidad INTEGER,
        precio REAL
    )
    """)

    # compras
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compra(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        UNIQUE(codigo_generacion)
    )
    """)

    # Detalle
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_compra(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_compra INTEGER,
        id_producto INTEGER,
        cantidad INTEGER,
        precio_unitario REAL,
        subtotal REAL
    )
    """)

    #Detalle_Clasificador
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_clasificador(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_tipo_documento INTEGER NOT NULL,
        id_clase_documento INTEGER NOT NULL,
        id_clasificacion INTEGER NOT NULL,
        id_sector INTEGER NOT NULL,
        id_tipo_costo_gasto INTEGER NOT NULL,
        id_tipo_operacion INTEGER NOT NULL
    )
    """)

    #Periodos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS periodo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        anio INTEGER     
    )
    """)

    conn.commit()
    conn.close()