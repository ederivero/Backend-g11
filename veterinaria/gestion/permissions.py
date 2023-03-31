from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from .models import Usuario

class SoloClientes(BasePermission):
    # podemos modificar el mensaje que queremos indicar si el usuario no tiene los permisos suficientes
    message = 'Solo los clientes pueden realizar esta peticion'


    def has_permission(self, request: Request, view):
        # request.user > toda la informacion del usuario autenticado
        usuario : Usuario = request.user

        # utilizando un operador ternario
        # return True if usuario.tipoUsuario == 'CLIENTE' else False
        
        # sin el uso de un operador ternario
        if usuario.tipoUsuario == 'CLIENTE':
            # si retornamos True indica que el usuario tiene los permisos correspondientes
            return True

        else:
            return False