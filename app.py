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


@app.route("/gatito/<int:id>", methods=["POST"])
def add_by_id(id):
    found_gatito = None
    
    for gatito in GATITOS:
        if int(gatito.get("id")) == id:
            found_gatito = gatito
            break

    if not found_gatito:
        return {"error": "No se encontró el gatito"}, 404

    params = request.args
    
    found_gatito["nombre"] = params.get("nombre", found_gatito["nombre"])
    edad = safe_int(params.get("edad"), found_gatito["edad"])
    if edad is None:
        return {"error": "El parámetro 'edad' debe ser un número entero"}, 400
    found_gatito["edad"] = edad
    found_gatito["raza"] = params.get("raza", found_gatito["raza"])
    found_gatito["color"] = params.get("color", found_gatito["color"])
    found_gatito["vacunado"] = (
        str_to_bool(params.get("vacunado"))
        if params.get("vacunado")
        else found_gatito["vacunado"]
    )
    found_gatito["esterilizado"] = (
        str_to_bool(params.get("esterilizado"))
        if params.get("esterilizado")
        else found_gatito["esterilizado"]
    )

    return {"message": "Gatito actualizado", "gatito": found_gatito}


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