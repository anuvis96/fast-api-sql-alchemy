#configuracion que nos va permitir conectarnos a MYSQL

#modulo que nos permite interactuar con la bd> SqlAlchemy ORM 

#utiliza librerias como pymsql para conectarse a cualquier db


from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:password@localhost:3307/prueba")
meta = MetaData()

conn = engine.connect() #metodo llamado connect(devuelve objeto de conexion) guardada en la var conn
