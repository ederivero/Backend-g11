from sqlalchemy import Column, types
from enum import Enum
from sqlalchemy.sql.schema import ForeignKey
from bd import conexion

# Para cuando nosotros queremos utilizar un enumerable en una columna de la bd tenemos que crear una clase definiendo esos enumerables
class EstadoTareaEnum(Enum):
    # https://docs.python.org/3/library/enum.html
    PENDIENTE = 'PENDIENTE'
    REALIZANDOSE = 'REALIZANDOSE'
    REALIZADA = 'REALIZADA'
    CANCELADA = 'CANCELADA'

class Tarea(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_= types.Text, default='No tiene descripcion')
    fechaVencimiento = Column(type_=types.DateTime, name='fecha_vencimiento')
    estado = Column(type_=types.Enum(EstadoTareaEnum), default=EstadoTareaEnum.PENDIENTE)

    usuarioId = Column(ForeignKey(column='usuarios.id'), type_=types.Integer, nullable=False, name= 'usuario_id')

    __tablename__ = 'tareas'