# ==========================================================
# MODELO TACO
# ==========================================================

from flask_app.config.mysqlconnection import connectToMySQL


class Taco:

    def __init__(self, data):
        self.id = data.get("id")
        self.tortilla = data.get("tortilla")
        self.guiso = data.get("guiso")
        self.salsa = data.get("salsa")
        self.restaurante_id = data.get("restaurante_id")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    # ======================================================
    # CREATE - GUARDAR UN NUEVO TACO
    # ======================================================

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO tacos (tortilla, guiso, salsa, restaurante_id)
            VALUES (%(tortilla)s, %(guiso)s, %(salsa)s, %(restaurante_id)s);
        """
        return connectToMySQL("esquema_tacos").query_db(query, datos)

    # ======================================================
    # READ - OBTENER TODOS LOS TACOS
    # ======================================================

    @classmethod
    def get_all(cls):
        query = """
            SELECT id, tortilla, guiso, salsa, restaurante_id, created_at, updated_at
            FROM tacos
            ORDER BY id DESC;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query)

        tacos = []
        if resultados:
            for taco in resultados:
                tacos.append(cls(taco))

        return tacos