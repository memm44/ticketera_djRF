
Ticketera sencilla desarrollada con Django 2.2 y Django rest framework.


-----------------------------------------------------------------------------------------------------------------


EndPoint de ejemplo para crear un Issue:[POST] por defecto 
se crean con fecha y hora actualy el estado en false indicando que no se ha resuelto
ruta ejemplo: http://localhost:8000/issues
{ 
"id_issuer":"AA5647B8", 
"issue": "los baños están sucios"
}
-----------------------------------------------------------------------------------------------------------------
Endpoint de ejemplo para Asignar o actualizar un ticket :[PATCH]
Nota: Los empleados deben estar creados primero en la base de datos para luego asociarles un id de Issue
ruta ejemplo: http://localhost:8000/issue/assign
{
	"id":1,
	"status":true,
	"id_issuer":"AA5647B8",
	"id_responsible":"luis"
}



Endpoint de ejemplo para Consultar y listar o actualizar el status de un Issue especifico a traves de su id. : [GET]
rutas ejemplo: 
http://localhost:8000/issue/1/     [esta ruta devuelve un registro especifico dependiendo del parametro que pasemos en la url]

http://localhost:8000/issues    [esta ruta lista todos los issues con su informacion especifica]
ejemplo de la devoluvción:
 {
        "id": 14,
        "issue": "los baños están sucios",
        "id_issuer": "AA5647B8",
        "status": true,
        "created_at": "2020-03-08T21:23:20.433006-03:00",
        "modified_at": "2020-03-08T21:27:21.004979-03:00",
        "id_responsible": "jorge"
    }

Endpoint para eliminar un ticket [Delete]
ruta de ejemplo:
http://localhost:8000/issue/1/

