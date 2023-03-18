from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.categoria_model import Categoria

class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria