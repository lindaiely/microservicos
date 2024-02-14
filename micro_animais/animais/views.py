from django.shortcuts import render
from rest_framework import viewsets
from animais.models import Animal
from animais.serializers import AnimalSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

def home(request):
    return HttpResponse("Bem-vindo à API de Animais!")


@api_view(['GET'])
def listar_animais_com_adocoes(request):
    # Fazer a chamada de API para obter a lista de adoções do microserviço de adoção
    response_adocoes = requests.get("http://localhost:8001/adocoes/")
    
    # Fazer a chamada de API para obter a lista de animais
    animais = Animal.objects.all()
    animais_serialized = AnimalSerializer(animais, many=True).data

    # Verificar se as chamadas foram bem-sucedidas (código de resposta 200)
    if response_adocoes.status_code == 200:
        adocoes = response_adocoes.json()
        return Response({"animais": animais_serialized, "adocoes": adocoes})
    else:
        # Se alguma das chamadas falhou, retornar uma resposta de erro
        return Response({"erro": "Falha ao obter lista de adoções e/ou animais"}, status=500)