from rest_framework import serializers

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)