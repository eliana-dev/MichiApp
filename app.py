from flask import Flask, request
from models.data import GATITOS
from utils.validation import str_to_bool, safe_int

app = Flask(__name__)


@app.route("/gatito", methods=["GET"])
def get_kittens():
    return GATITOS


@app.route("/gatito/<int:id>", methods=["GET"])
def get_by_id(id):
    found_gatitos = []
    for gatito in GATITOS:
        if int(gatito.get("id")) == id:
            found_gatitos.append(gatito)

    if found_gatitos:
        return {
            "Mensaje": f"Se encontraron {len(found_gatitos)} con el id {id}",
            "Coincidencias": found_gatitos,
        }
    else:
        return {"error": "Gatito no encontrado"}, 404


@app.route("/gatito", methods=["POST"])
def add_gatito():
    params = request.args
    id_gatito = safe_int(params.get("id"))
    if id_gatito is None:
        return {"error": "El parámetro 'id' debe ser un número entero"}, 400
    nombre = params.get("nombre")
    if not nombre:
        return {"error": "El parámetro 'nombre' es obligatorio"}, 400
    edad = safe_int(params.get("edad"))
    if edad is None:
        return {"error": "El parámetro 'edad' debe ser un número entero"}, 400

    raza = params.get("raza", "desconocida")
    color = params.get("color", "desconocido")
    vacunado = str_to_bool(params.get("vacunado"))
    esterilizado = str_to_bool(params.get("esterilizado"))

    record = {
        "id": id_gatito,
        "nombre": nombre,
        "edad": edad,
        "raza": raza,
        "color": color,
        "vacunado": vacunado,
        "esterilizado": esterilizado,
    }

    GATITOS.append(record)

    return {"mensaje": "Gatito agregado con éxito", "gatito": record}, 201


@app.route("/gatito/<int:id>", methods=["PUT"])
def replace_gatito(id):
    found_gatito = next((g for g in GATITOS if int(g.get("id")) == id), None)
    if not found_gatito:
        return {"error": "No se encontró el gatito"}, 404

    params = request.args

    required_fields = ["nombre", "edad", "color"]
    for field in required_fields:
        if field not in params:
            return {"error": f"Falta el parámetro obligatorio '{field}'"}, 400

    nombre = params.get("nombre")
    edad = safe_int(params.get("edad"))
    if edad is None:
        return {"error": "El parámetro 'edad' debe ser un número entero"}, 400

    raza = params.get("raza", "desconocida")
    color = params.get("color")

    try:
        vacunado = str_to_bool(params.get("vacunado", False))
        esterilizado = str_to_bool(params.get("esterilizado", False))
    except ValueError:
        return {
            "error": "Los parámetros 'vacunado' y 'esterilizado' deben ser true/false o 1/0"
        }, 400

    found_gatito.update(
        {
            "nombre": nombre,
            "edad": edad,
            "raza": raza,
            "color": color,
            "vacunado": vacunado,
            "esterilizado": esterilizado,
        }
    )

    return {"message": "Gatito reemplazado con éxito", "gatito": found_gatito}


@app.route("/gatito/<int:id>", methods=["DELETE"])
def delete_by_id(id):
    gatitos_eliminados = []

    for i in range(len(GATITOS) - 1, -1, -1):
        if GATITOS[i].get("id") == id:
            gatitos_eliminados.append(GATITOS.pop(i))

    if not gatitos_eliminados:
        return {"error": "No se encontraron gatitos con ese id!"}, 404

    return {
        "mensaje": f"Se eliminaron {len(gatitos_eliminados)} gatitos con id {id}",
        "gatitos_eliminados": gatitos_eliminados,
    }


if __name__ == "__main__":
    app.run(debug=True)
