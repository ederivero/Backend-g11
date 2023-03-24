from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Categoria
from .serializers import PruebaSerializer, CategoriaSerializer

class PruebaView(APIView):
    def get(self, request):
        data = [ {
            'nombre': 'diversion',
            'id': 1
        }, {
            'nombre': 'entretenimiento',
            'id': 2
        }]

        return Response(data= data)

    def post(self, request: Request):
        # https://www.django-rest-framework.org/api-guide/requests/
        print(request.data)
        data= request.data
        data_serializada = PruebaSerializer(data = data)
        # retornara Verdadero o Falso si la data es correcta
        resultado = data_serializada.is_valid()

        if resultado is True:
            return Response(data= {
                'message': 'Se recibio la prueba'
            })
        else:
            return Response(data= {
                'message': 'La data es invalida',
                # errors > me mostrar los errores que generaro que la data sea incorrecta al momento de serializar
                'content': data_serializada.errors
            })


class CategoriaView(APIView):
    def post(self, request: Request):
        data = request.data
        data_serializada = CategoriaSerializer(data=data)

        resultado = data_serializada.is_valid()
        if resultado:
            print(data_serializada.validated_data)
            nueva_categoria = Categoria(**data_serializada.validated_data)
            # save() > guardar la nueva informacion en la base de datos de manera permanente
            nueva_categoria.save()

            return Response(data={
                'message': 'Categoria creada exitosamente'
            })
        
        else:
            return Response(data={
                'message': 'Error al crear la categoria',
                'content': data_serializada.errors
            })