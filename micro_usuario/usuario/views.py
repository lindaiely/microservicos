from django.shortcuts import render
from rest_framework import viewsets
from usuario.models import Usuario
from usuario.serializers import UsuarioSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def home(request):
    return HttpResponse("Bem-vindo à API do Usuário!")

@api_view(['GET'])
def listar_usuarios_com_animais(request):
    # Fazer a chamada de API para obter a lista de animais do microserviço de animais
    response_animais = requests.get("http://localhost:8003/animais/")
    
    # Fazer a chamada de API para obter a lista de usuários
    usuarios = Usuario.objects.all()
    usuarios_serialized = UsuarioSerializer(usuarios, many=True).data

    # Verificar se as chamadas foram bem-sucedidas (código de resposta 200)
    if response_animais.status_code == 200:
        animais = response_animais.json()
        return Response({"usuarios": usuarios_serialized, "animais": animais})
    else:
        # Se alguma das chamadas falhou, retornar uma resposta de erro
        return Response({"erro": "Falha ao obter lista de animais e/ou usuários"}, status=500)
