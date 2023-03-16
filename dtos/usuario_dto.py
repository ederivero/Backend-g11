from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuario_model import Usuario

class UsuarioDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario