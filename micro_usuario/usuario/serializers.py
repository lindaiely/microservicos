from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.email = validated_data.get('email', instance.email)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.genero = validated_data.get('genero', instance.genero)
        instance.save()
        return instance