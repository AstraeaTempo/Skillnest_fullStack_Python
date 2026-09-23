# ==========================================================
# MYSQL CONNECTION
# ==========================================================

import pymysql.cursors

class MySQLConnection:
    """
    Administra la conexión con una base de datos MySQL.
    """

    def __init__(self, db):
        """
        Recibe el nombre de la base de datos y establece una conexión.
        """
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",  # Cambia esto por tu contraseña de MySQL
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """
        Ejecuta una consulta SQL.
        """
        with self.connection.cursor() as cursor:
            try:
                print("Running Query:")
                print(query)

                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    resultados = cursor.fetchall()
                    return resultados

                elif query.strip().lower().startswith("insert"):
                    return cursor.lastrowid

                else:
                    return None

            except Exception as e:
                print("Something went wrong:")
                print(e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    """
    Recibe el nombre de una base de datos y devuelve
    una instancia de MySQLConnection.
    """
    return MySQLConnection(db)