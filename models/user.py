from curses import meta
from tokenize import String
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

# primero se llama users en mysql, luego meta = sqlalchemy sepa mas propiedades de la tabla, especifico columna
users = Table("users", meta, Column(
    "id", Integer, primary_key=True), Column("name", String(255)), Column("email", String(255)), Column("password", String(255)))


# unir a la conexion que tenemos para ello utilizamos la etiqueta meta
# ya tenemos el schema, utilizando el engine(se conecta a la uri de mysql) para generar la tabla

meta.create_all(engine) 