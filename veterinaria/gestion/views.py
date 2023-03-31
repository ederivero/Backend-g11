from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import RegistroUsuarioSerializer
from .models import Usuario
from rest_framework.response import Response
from rest_framework import status

class RegistroUsuario(APIView):

    def post(self, request: Request):
        serializador = RegistroUsuarioSerializer(data = request.data)
        if serializador.is_valid():
            password = serializador.validated_data.get('password')
            nuevo_usuario = Usuario(**serializador.validated_data)
            # generar el hash de la password
            nuevo_usuario.set_password(password)

            nuevo_usuario.save()

            return Response(data={
                'message': 'Usuario creado exitosamente'
            },status=status.HTTP_201_CREATED)
        
        else:
            return Response(data={
                'message': 'Error al crear el usuario',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)