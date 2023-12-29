from django.shortcuts import render
from rest_framework import viewsets
from animais.models import Animal
from animais.serializers import AnimalSerializer
from django.http import HttpResponse

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

def home(request):
    return HttpResponse("Bem-vindo à API de Animais!")