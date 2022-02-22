from fastapi import FastAPI
from routes.user import user

app = FastAPI() #utilizar modulo de fastapi para crear server basico


app.include_router(user) #Quiero que la aplicacion incluya las rutas que vienen desde user

