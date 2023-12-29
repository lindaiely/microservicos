from django.shortcuts import render
from rest_framework import viewsets
from usuario.models import Usuario
from usuario.serializers import UsuarioSerializer
from django.http import HttpResponse

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def home(request):
    return HttpResponse("Bem-vindo à API do Usuário!")
