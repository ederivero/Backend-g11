from flask_restful import Resource, request
from bcrypt import hashpw, gensalt
from dtos.usuario_dto import UsuarioDto
from models.usuario_model import Usuario
from bd import conexion

class UsuariosController(Resource):
    def post(self):
        data = request.json
        dto = UsuarioDto()
        try:
            data_validada = dto.load(data)
            # Generar el hash de la password 
            salt = gensalt(rounds=10)
            password = bytes(data_validada.get('password'),'utf-8')
            password_hashed = hashpw(password, salt)
            password_hashed_str = password_hashed.decode('utf-8')

            nuevo_usuario = Usuario(
                correo = data_validada.get('correo'), 
                password= password_hashed_str, 
                nombre = data_validada.get('nombre'), 
                apellido = data_validada.get('apellido'))

            conexion.session.add(nuevo_usuario)
            conexion.session.commit()

            return {
                'message': 'Usuario creado exitosamente'
            }
        except Exception as error:
            return {
                'message': 'Error al ingresar el usuario',
                'content': error.args
            }

