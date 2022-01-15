# main.py
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.post("/almacena")
def add(string):
    dataBase = open("data.txt", "a")
    dataBase.write(string + "\n")
    dataBase.close()
    return {"msg" : "Sentence added succesfully"}

@app.get("/consulta")
def buscar(string):
    #troceamos para ignorar saltos de línea
    dataBase = open("data.txt", "r").read().splitlines()
    i = 0
    #quitamos los tildes con el metodo maketrans (traduccion)
    a,b = 'áéíóú','aeiou'
    trans = str.maketrans(a,b)
    for line in dataBase:
	    new_line = line.lower() #no tomamos en cuenta minusculas
	    new_line = new_line.translate(trans)
	    if (string in new_line):
		    i += 1 

    return {"number" : i}

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=12345)
