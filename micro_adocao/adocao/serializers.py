from rest_framework import serializers
from .models import Adocao

class AdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocao
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.animal_nome = validated_data.get('animal_nome', instance.animal_nome)
        instance.adotante_nome = validated_data.get('adotante_nome', instance.adotante_nome)
        instance.data_adocao = validated_data.get('data_adocao', instance.data_adocao)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance