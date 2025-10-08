import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vehiculosbd"
    )
    cursor=conexion.cursor(buffered=True)
    print("exito")
except Exception as e:
    print(f"Ocurrio un error con la DB verifique {e}")    