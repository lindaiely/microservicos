from django.shortcuts import render
from rest_framework import viewsets
from adocao.models import Adocao
from adocao.serializers import AdocaoSerializer
from django.http import HttpResponse

class AdocaoViewSet(viewsets.ModelViewSet):
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer

def home(request):
    return HttpResponse("Bem-vindo à API de Adoções!")
