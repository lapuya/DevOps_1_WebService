## DevOps A1 - Servicio Web
_Esta actividad consiste en crear un servicio web sencillo._

### Requisitos 📋
El enunciado es el siguiente:
*Se pide al alumno programar un servicio web. Este servicio web deberá escuchar en el puerto 12345 y expondrá dos endpoints:

El primero recibe una cadena de caracteres, de longitud arbitraria, y la almacena en un fichero en disco.
El segundo recibirá una única palabra (sin espacios). Se devolverá el número total de las cadenas del citado fichero que la contengan, sin tener en cuenta:
 · Mayúsculas (CADENA == Cadena).
 · Posibles acentos (avión == Avion).
Múltiples apariciones en la misma cadena cuentan como una única.
Como requisito, el fichero donde se guardan los datos se debe persistir en disco y leerlo al arrancar el proceso. Si no existe, se creará vacío.*

### Pre-requisitos 🔧
Existía libertad de elección del lenguaje, si bien se recomendaba JAVA o Python. Finalmente se ha optado por realizarlo en **Python**.

* Python 3
* pipenv -> para la creación de un entorno virtual
* uvicorn -> servidor ASGI para servir nuestra API
* FastAPI -> framework para crear REST APIs

Se recomendaba el uso de Flask, pero finalmente se ha decidido probar FastAPI

