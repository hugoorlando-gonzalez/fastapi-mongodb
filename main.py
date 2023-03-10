from fastapi import FastAPI

# accedemos al contexto inicial de FastAPI, de como se va a comportar nuestro servidor al recibir peticiones
app = FastAPI() 

@app.get("/")
# siempre que llamamos a un server, la función debe ser asincronica
# async significa que cuando hacemos una petición, la app no puede hacer nada hasta que retorne algo el servidor
async def root():
  return {"message": "Hi from FastAPI"}


# protocolo http es un estándar que nos permite "hablar" a través de la red

