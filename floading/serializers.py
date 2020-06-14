from rest_framework import serializers
from .models import endereco

class enderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = endereco
        fields = ['Name', 'Value']