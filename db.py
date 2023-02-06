from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#engine permite a SQLAlachemy comunicarser con la base de datos
#https://docs.sqlalchemy.org/en/14/core/enigne.html
#engine
engine = create_engine('sqlite:///database/tareas.db', connect_args={"check_same_thread":False})
#crear el engine no conecta directamente a la bd


#sesion, la creamos para poder realacion trasacciones
Session = sessionmaker(bind=engine)
session = Session()

#vinculacion, añadimos esta varaible para mapear y vincular
Base = declarative_base()
