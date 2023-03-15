from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_enum import EnumField
from models.tarea_model import Tarea, EstadoTareaEnum

class TareaDto(SQLAlchemyAutoSchema):
    estado = EnumField(enum=EstadoTareaEnum, by_value=True)

    class Meta:
        model = Tarea