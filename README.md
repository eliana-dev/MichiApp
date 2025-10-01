# MichiApp 😺

API RESTful básica utilizando Flask que permite realizar operaciones CRUD sobre una lista de **gatitos**.

![Python](https://img.shields.io/badge/python-336fa0?style=for-the-badge&logo=python&logoColor=336fa0&labelColor=white)
![Flask](https://img.shields.io/badge/flask-blue?style=for-the-badge&logo=flask&logoColor=blue&labelColor=white)

## Endpoints implementados

`GET /gatito`: Devuelve una lista de todos los gatitos.

![GET/gatito](assets\get-all.png "GET")

`GET /gatito/<id>`: Devuelve los detalles de un específico por su id.

![GET/gatito/id](assets\get-id.png "GET")

`POST /gatito`: Crea un nuevo gatito, los datos del nuevo gatito se pasan como query params.

![POST/gatito/](assets\post.png "POST")

`PUT /gatito/<id>`: Actualiza los detalles de un gatito existente por su id.

![PUT/gatito/id](assets\put.png "PUT")

`DELETE /gatito/<id>`: Elimina un gatito por su id.

![DELETE/gatito/id](assets\delete.png "DELETE")

Utiliza un almacenamiento en memoria (Lista de diccionarios) para guardar los datos en memoria.
