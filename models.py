from sqlalchemy import Column,Integer,String,Boolean
import db


class Tarea(db.Base):
    #formulacion para generar la db
    __tablename__ = "tarea"
    __table_args__ = {"sqlite_autoincrement": True} #automaticamente la PK se autoincrementa
    id_tarea = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False) #esta campo no puede estar vacio
    hecha = Column(Boolean) #falso de inicio.
    categoria = Column(String(15)) #categoria se determino 15 de len
    fecha = Column(Integer) #formato dd-mm-yy

    def __init__(self, contenido, hecha, categoria, fecha):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.fecha = fecha

    def __str__(self):
        return "Tarea({} -> {} -> {} -> {} -> {})".format(self.id_tarea, self.contenido, self.hecha,
                                                          self.hecha, self.contenido)


