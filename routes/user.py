from calendar import c
from fastapi import APIRouter #te permite definir rutas por separado
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet #modulo que permite cifrar

user = APIRouter()
key = Fernet.generate_key()#inicializar para utilizarlo, generate_key(genera string con caracteres aleatorios)
# key me sirve para hacer unico cada uno de los cifrados que haga
f = Fernet(key) #con esta funcion puedo cifrar lo que quiera

@user.get("/users") #ruta inicial es decir el decorador @
def get_users():
    return conn.execute(users.select()).fetchall() #retorna consulta db, como tenemos sqlalchemy utiliza el modelo de la tabla y con fetch_all() traigo todos los datos


@user.post("/users") #ruta inicial es decir el decorador @
def create_user(user: User): #guardar un dato entro de la tabla, recibe un dato tipo usuario que viene de los schemas
    new_user = {"name": user.name, "email":user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8")) #encrypt para encriptar la contraseña, ademas transformar el pass a codificacion utf-8
    response = conn.execute(users.insert().values(new_user)) #inserto el dato en la bd pasandole los valores(new_user)
    print(response.lastrowid)
    return "received"


@user.get("/users") #ruta inicial es decir el decorador @
def hola():
    return "hello world"

@user.get("/users") #ruta inicial es decir el decorador @
def hola():
    return "hello world"

@user.get("/users") #ruta inicial es decir el decorador @
def hola():
    return "hello world"            