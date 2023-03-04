from base_de_datos import conexion
from sqlalchemy import Column, types

class Maestro(conexion.Model):
    id = Column(type_= types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellidos = Column( type_=types.Text)
    correo = Column(type_= types.Text, unique=True, nullable=False)
    direccion = Column(type_=types.Text)

    __tablename__ = 'maestros'