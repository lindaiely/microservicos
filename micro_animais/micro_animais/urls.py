"""
URL configuration for micro_animais project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from animais.views import AnimalViewSet, home, listar_animais_com_adocoes

router = DefaultRouter()
router.register(r'animais', AnimalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', home, name='home'),
    path('animais/', AnimalViewSet.as_view({'get': 'list', 'post': 'create'}), name='animais-list-create'),
    path('animais-com-adocoes/', listar_animais_com_adocoes),
]