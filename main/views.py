from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer
from .models import Funcionarios
from .serializers import FuncionarioSerializer
from rest_framework import viewsets

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionarioSerializer