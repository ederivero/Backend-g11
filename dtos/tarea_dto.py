from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_enum import EnumField
from models.tarea_model import Tarea, EstadoTareaEnum
from marshmallow import Schema, fields

class TareaDto(SQLAlchemyAutoSchema):
    estado = EnumField(enum=EstadoTareaEnum, by_value=True)

    class Meta:
        model = Tarea
    

class TareaFiltros(Schema):
    descripcion = fields.Str(required=False)
    estado = EnumField(enum=EstadoTareaEnum)
    fechaVencimiento = fields.DateTime(required=False)
    usuarioId = fields.Int(required=True)