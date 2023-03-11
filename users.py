from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user

# BaseModel nos da la capacidad de crear una entidad y tratarlos de diferentes formas
class User(BaseModel):
    # definimos los parametros que tendran los usuarios
    id: int
    name: str
    surname: str
    url: str
    age: int


# listado de datos falsos
users_fake_db = [
    User(id=1, name="Brais", surname="moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev", url="https://moure.dev", age=33),
    User(id=3, name="Haakon", surname="Dev", url="", age=20)

]


@app.get("/usersjson")
async def users():
    return [
        {
            "name": "Brais",
            "surname": "moure",
            "url": "https://moure.dev",
            "age": 35
        },
        {
            "name": "Moure",
            "surname": "Dev",
            "url": "https://moure.dev",
            "age": 20
        },
        {
            "name": "Haakon",
            "surname": "Dahlberg",
            "url": "https://hakoon.com",
            "age": 33
        }
    ]


@app.get("/users")
async def users():
    return users_fake_db

# Path
# http://localhost:8000/users/2
@app.get("/users/{id}")
async def user_by_id(id: int):
    return search_user(id)


# Query
# http://localhost:8000/users/?id=2
@app.get("/users/")
async def user_by_id(id: int):
    return search_user(id)


# http://localhost:8000/api/users/2
@app.get("/api/users/{id}")
async def user_by_id(id: int):
    return search_user(id)


# Agregar usuarios
@app.post("/users/")
async def add_user(user: User):  # parametro user de tipo User
    user_id = search_user(user.id)

    # comprobamos que el usuario exista, si existe, retorna un mensaje de error
    if type(user_id) == User:
        return {"message": "El usuario ya existe"}

    users_fake_db.append(user)
    return user

@app.put("/users/")
async def update_user(user: User):
    found = False

    for index, saved_user in enumerate(users_fake_db):
        if saved_user.id == user.id:
            users_fake_db[index] = user
            found = True

    if not found:
        return {"message": "No se ha actualizado al usuario"}
    else:
        return user

@app.delete("/users/{id}")
async def user_by_id(id: int):
    found = False

    for index, user in enumerate(users_fake_db):
        if user.id == id:
            del users_fake_db[index]
            found = True

    if not found:
        return {"message": "No se ha actualizado al usuario"}
    else:
        return user


def search_user(id: int):
    users = list(filter(lambda item: item.id == id, users_fake_db))

    try:
        return users[0]
    except:
        return {"message": "No se ha encontrado al usuario"}
