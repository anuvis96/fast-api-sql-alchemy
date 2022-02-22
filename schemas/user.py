
from typing import Optional # forma de traer tipos de datos
from pydantic import BaseModel  # manera de modelar los datos, crear tipos de datos


class User(BaseModel):  # Clase User basada en el modelo base
    id: Optional[str]
    name: str
    email: str
    password: str
