from rest_framework.serializers import ModelSerializer
from .models import Usuario

class RegistroUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
