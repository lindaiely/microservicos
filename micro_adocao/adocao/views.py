from django.shortcuts import render
from rest_framework import viewsets
from adocao.models import Adocao
from adocao.serializers import AdocaoSerializer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

class AdocaoViewSet(viewsets.ModelViewSet):
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer

def home(request):
    return HttpResponse("Bem-vindo à API de Adoções!")

@api_view(['GET'])
def listar_adocoes_com_usuarios(request):
    # Fazer a chamada de API para obter a lista de usuários do microserviço de usuário
    response_usuarios = requests.get("http://localhost:8002/usuarios/")
    
    # Fazer a chamada de API para obter a lista de adoções
    adocoes = Adocao.objects.all()
    adocoes_serialized = AdocaoSerializer(adocoes, many=True).data

    # Verificar se as chamadas foram bem-sucedidas (código de resposta 200)
    if response_usuarios.status_code == 200:
        usuarios = response_usuarios.json()
        return Response({"usuarios": usuarios, "adocoes": adocoes_serialized})
    else:
        # Se alguma das chamadas falhou, retornar uma resposta de erro
        return Response({"erro": "Falha ao obter lista de usuários e/ou adoções"}, status=500)
