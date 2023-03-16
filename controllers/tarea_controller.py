from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import Query
from models.tarea_model import Tarea
from bd import conexion
from dtos.tarea_dto import TareaDto, TareaFiltros

class TareasController(Resource):
    @jwt_required()
    def post(self):
        usuario_id = get_jwt_identity()
        data = request.json
        dto = TareaDto()
        try:
            data_validada = dto.load(data)
            nueva_tarea = Tarea(**data_validada, usuarioId = usuario_id)
            conexion.session.add(nueva_tarea)
            conexion.session.commit()

            return {
                'message': 'Se agrego la tarea exitosamente'
            }, 201
        except Exception as error:
            return {
                'message': 'Error al crear la tarea',
                'content': error.args
            }

        
    @jwt_required()
    def get(self):
        # TODO: devolver todas las tareas del usuario
        usuario_id = get_jwt_identity()
        query:Query = conexion.session.query(Tarea)
        data = query.filter_by(usuarioId = usuario_id).all()
        dto = TareaDto()
        resultado = dto.dump(data, many=True)

        return {
            'content': resultado
        }

class TareaController(Resource):
    @jwt_required()
    def get(self):
        usuario_id = get_jwt_identity()
        # TODO: utilizando query params poder recibir el nombre, fecha_vencimiento o el estado y devolver solamente esas tareas con esos filtros especializados solo del usuario
        query_params = request.args.to_dict().copy()
        query_params['usuarioId'] = usuario_id
        try:
            dto = TareaFiltros()
            parametros = dto.load(query_params)
            query:Query = conexion.session.query(Tarea)
            data = query.filter_by(**parametros).all()
            # /tarea?nombre=Ir a la piscina 
            # /tarea?estado=REALIZANDOSE
            # /tarea?fecha_vencimiento=2023-07-31 14:55:25
            # /tarea?nombre=Playaso&estado=PENDIENTE
            # if - elif - else
            dto = TareaDto()
            resultado = dto.dump(data, many=True)
            return {
                'content': resultado
            }
        except Exception as e:
                return {
                    'message': 'Error al hacer la busqueda',
                    'content': e.args
                }