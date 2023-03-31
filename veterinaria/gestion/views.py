from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import RegistroUsuarioSerializer
from .models import Usuario
from rest_framework.response import Response
from rest_framework import status
# https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework.permissions import IsAuthenticated
from .permissions import SoloClientes
from cloudinary import uploader

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
        

class PerfilUsuario(APIView):
    # lo hara en orden > > > primero entrara al permiso de IsAuthenticate y luego si esta todo bien pasara al segundo permiso y asi sucesivamente, si algun permiso falla absolutamente se detiene todos los demas permisos
    permission_classes = [IsAuthenticated, SoloClientes]

    def get(self, request: Request):
        print(request.user)
        print(request.auth)
        # TODO: Devolver el usuario, NO DEVOLVER LA PASSWORD solamente el nombre, apellido, correo y tipoUsuario utilizando un serializador
        return Response(data={
            'content': ''
        })

class Mascotas(APIView):
    permission_classes = [IsAuthenticated, SoloClientes]

    def post(self, request:Request):
        foto = request.FILES.get('foto')
        print(foto)
        resultado = uploader.upload(foto)

        return Response(data= {
            'message': 'Mascota creada exitosamente',
            'content': resultado
        }, status=status.HTTP_201_CREATED)