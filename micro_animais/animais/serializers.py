from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

    def update(self, instance, validated_data):
            instance.nome = validated_data.get('nome', instance.nome)
            instance.especie = validated_data.get('especie', instance.especie)
            instance.idade = validated_data.get('idade', instance.idade)
            instance.descricao = validated_data.get('descricao', instance.descricao)
            instance.save()
            return instance