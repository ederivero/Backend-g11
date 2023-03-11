from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.tarea_model import Tarea

class TareaDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea