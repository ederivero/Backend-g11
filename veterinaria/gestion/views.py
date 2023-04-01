from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import RegistroUsuarioSerializer, MascotasSerializer
from .models import Usuario, Mascota
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
    
from pprint import pprint
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

class MascotasView(APIView):
    permission_classes = [IsAuthenticated, SoloClientes]

    def post(self, request:Request):
        # foto = request.FILES.get('foto')
        # resultado = uploader.upload(foto)
        try:
          data = {
              'nombre': request.data.get('nombre'),
              'sexo': request.data.get('sexo'),
              'fechaNacimiento': request.data.get('fechaNacimiento'),
              'alergias': request.data.get('alergias'),
              'foto': request.FILES.get('foto'),
              'cliente': request.data.get('cliente')
          }

          serializador = MascotasSerializer(data=data)
          if serializador.is_valid():
              serializador.save()
              return Response(data= {
                  'message': 'Mascota creada exitosamente',
                  'content': serializador.data
              }, status=status.HTTP_201_CREATED)
          else:
              return Response(data={
                  'message': 'Error al crear mascota',
                  'content': serializador.errors
              }, status=status.HTTP_400_BAD_REQUEST)
          
        except Exception as e:
          return Response(data={
              'message': 'Error al crear mascota',
              'content': str(e)
          }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request:Request):
        mascotas = Mascota.objects.all()
        serializador = MascotasSerializer(mascotas, many=True)

        return Response(data = {
            'content': serializador.data
        }, status=status.HTTP_200_OK)