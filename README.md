## DevOps A1 - Servicio Web
_Esta actividad consiste en crear un servicio web sencillo._

### Requisitos 📋
_Se pide al alumno programar un servicio web. Este servicio web deberá escuchar en el puerto 12345 y expondrá dos endpoints:_

_El primero recibe una cadena de caracteres, de longitud arbitraria, y la almacena en un fichero en disco.
El segundo recibirá una única palabra (sin espacios). Se devolverá el número total de las cadenas del citado fichero que la contengan, sin tener en cuenta:
 · Mayúsculas (CADENA == Cadena).
 · Posibles acentos (avión == Avion).
Múltiples apariciones en la misma cadena cuentan como una única.
Como requisito, el fichero donde se guardan los datos se debe persistir en disco y leerlo al arrancar el proceso. Si no existe, se creará vacío._

### Pre-requisitos 🔧
Existía libertad de elección del lenguaje, si bien se recomendaba JAVA o Python. Finalmente se ha optado por realizarlo en **Python**.

* Python 3
* pipenv -> para la creación de un entorno virtual
* uvicorn -> servidor ASGI para servir nuestra API
* FastAPI -> framework para crear REST APIs
* Línea de comandos bash

Se recomendaba el uso de Flask, pero finalmente se ha decidido probar FastAPI

### Pasos e instalación 
Instalación de pipenv usando _pip_:
´´´
sudo pip install pipenv
´´´
Después, instalaremos FastAPI y uvicorn:
´´´
pipenv install fastapi uvicorn
´´´
Y finalmente activamos el entorno virtual para tener acceso a los paquetes recién instalados:
´´´
pipenv shell
´´´
A partir de aquí ya podemos crear el ficher _.py_ y empezar a montar nuestro servidor.

