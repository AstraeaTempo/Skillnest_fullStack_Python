import pymysql.cursors

class MySQLConnection:
    """
    Administra la conexión entre Python y MySQL.
    """
    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",  # Ajusta tu contraseña de MySQL aquí
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """
        Ejecuta una consulta SQL.
        SELECT -> devuelve una lista de diccionarios.
        INSERT -> devuelve el ID generado (lastrowid).
        UPDATE/DELETE -> devuelve None.
        Error -> devuelve False.
        """
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                elif query.strip().lower().startswith("insert"):
                    return cursor.lastrowid

                else:
                    return None

            except Exception as e:
                print("Error al ejecutar la consulta:", e)
                return False

            finally:
                self.connection.close()

def connectToMySQL(db):
    """
    Función auxiliar para instanciar la conexión a la base de datos.
    """
    return MySQLConnection(db)