from sqlalchemy import Column , types

from db import conexion

class Categoria(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_ =types.Text, nullable=False)
    estado = Column(type_= types.Boolean, default=True)
    imagen = Column(type_= types.Text)

    __tablename__ = 'categorias'