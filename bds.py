import sqlite3 as sql

def crear_tablas():
    conn = sql.connect('database.db') # Si existe, se conecta a ella; si no existe, la crea
    # print("Base de datos abierta.") # muestra en la prompt este mensaje
    conn.execute('CREATE TABLE IF NOT EXISTS adivina_numero (fecha DATETIME, intentos INTEGER)') 
    conn.close() # cierra la conexion a la base de datos
    # print("Base de datos cerrada.")

def insert_adivina_numero(fecha,intentos):
    try: # Lo intentamos
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO adivina_numero (fecha, intentos) VALUES (?,?)",(fecha,intentos))
            con.commit()
        msg = "Se ha añadido el registro" # si lo conseguimos, saca un mensaje
    except: # Si no podemos insertar los datos en la base de datos
        con.rollback()
        msg = "Error al insertar los datos" # nos saca otro mensaje diferente
    return msg


def fetch_list(tabla):
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row # 
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {tabla}") # consultamos toda la lista de estudiantes / notas
        filas_bd = cur.fetchall();
        columnas_bd = [description[0] for description in cur.description] # Extraemos el nombre nombre de las columnas
    return filas_bd, columnas_bd