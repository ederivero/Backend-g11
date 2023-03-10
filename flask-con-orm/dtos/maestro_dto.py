from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.maestro_model import Maestro

class MaestroDto(SQLAlchemyAutoSchema): 
    class Meta:
       model = Maestro 