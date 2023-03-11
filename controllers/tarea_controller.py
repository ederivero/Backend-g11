from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.tarea_model import Tarea
from bd import conexion
from dtos.tarea_dto import TareaDto

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

        

    def get(self):
        # TODO: devolver todas las tareas del usuario
        pass

class TareaController(Resource):
    @jwt_required()
    def get(self):
        # TODO: utilizando query params poder recibir el nombre, fecha_vencimiento o el estado y devolver solamente esas tareas con esos filtros especializados solo del usuario
        # /tarea?nombre=Ir a la piscina
        # /tarea?estado=REALIZANDOSE
        # /tarea?fecha_vencimiento=2023-07-31 14:55:25
        # /tarea?nombre=Playaso&estado=PENDIENTE
        # if - elif - else
        
        pass