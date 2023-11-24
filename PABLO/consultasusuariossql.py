# CAMBIAR LAS VARIABLES ACORDE A NUESTROS DATOS

# Crear un nuevo cursor
cursor = conn.cursor()

# Preparar la consulta SQL para insertar datos
sql = "INSERT INTO tu_tabla (columna1, columna2) VALUES (%s, %s)"
valores = ('valor1', 'valor2')

# Ejecutar la consulta SQL
cursor.execute(sql, valores)

# Hacer commit para salvar los cambios
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()


