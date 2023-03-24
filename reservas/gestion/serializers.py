from rest_framework import serializers
from .models import Categoria

# https://www.django-rest-framework.org/api-guide/serializers/#serializers
class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'