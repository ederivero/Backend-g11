# TODO: Implementar para crear y listar a todos los maestros, utilizar o crear los DTOS correspondientes de los maestros
from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.maestro_model import Maestro
from dtos.maestro_dto import MaestroDto

class MaestroController(Resource):
    def get(self):
        query: Query = conexion.session.query(Maestro)
        resultado = query.all()
        dto = MaestroDto()
        maestros = dto.dump(resultado, many = True)
        return {
            'content': maestros
        }

    def post(self):
        data = request.json
        try:
            dto = MaestroDto()
            validated_data = dto.load(data)
            maestro = Maestro(nombre = validated_data.get('nombre'), 
                            apellidos = validated_data.get('apellidos'), 
                            correo = validated_data.get('correo'), 
                            direccion = validated_data.get('direccion'))
            conexion.session.add(maestro)
            conexion.session.commit()
            return {
                'message': 'Maestro creado exitosamente'
            }
        except Exception as error:
            return {
            'message': 'Error',
            'content': error.args
        }
