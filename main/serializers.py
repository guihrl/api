from rest_framework import serializers
from .models import Item
from .models import Funcionarios

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id', 'nome', 'descricao', 'valor'
]
        
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = [
            'id', 'nomeFuncionario', 'dataNascimento', 'eMail', 'salario'
        ]