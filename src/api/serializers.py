from .models import Funcionario, Perfil, Curriculo, Pessoa
from rest_framework import serializers




class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields =['id', 'nome', 'sobrenome', 'created_at', 'updated_at',
        'funcao', 'email', 'ano_nascimento']


class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields =['id', 'nome', 'sobrenome', 'created_at', 'updated_at',
        'email', 'github', 'avatar', 'celular', 'perfil'] 

class CurriculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields =['id', 'empresa', 'data_inicio', 'data_saida', 'empresa_atual',
        'resumo', 'created_at', 'updated_at',]
             