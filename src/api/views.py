

# Create your views here.

import email
from itertools import count
import json
from django.http import JsonResponse
from .models import Funcionario,Perfil,Curriculo
from .serializers import FuncionarioSerializer,PerfilSerializer, CurriculoSerializer
from src.api import serializers

def health(request):
    return JsonResponse({'mensagem': 'ok'} ,safe=False)

def funcionario_info(request):
    query_params = request.GET

    if request.method =='GET':
        qs_funcionario = Funcionario.objects.all().values()
        serializer = FuncionarioSerializer(qs_funcionario, many=True)
        return JsonResponse({"funcionarios": serializer.data})

    if request.method == 'POST':
        data = json.loads(request.body)

        funcionario = Funcionario()
        funcionario.ano_nascimento = data.get('ano_nascimento')
        funcionario.nome = data.get('nome')
        funcionario.sobrenome = data.get('sobrenome')
        funcionario.email = data.get('email')
        funcionario.funcao = data.get('funcao')

        existe_funcionario = Funcionario.objects.filter(email=funcionario.email).count()
        if existe_funcionario:
            return JsonResponse({"mensagem": "O usuário já existe"})
        
        cadastro = funcionario.save()
        serializer = FuncionarioSerializer(cadastro, many=False)
        return JsonResponse(serializer.data)

    if request.method == 'DELETE':
        existe_email = query_params.get('email')

        if existe_email:
            existe_funcionario = Funcionario.objects.filter(email=existe_email).first()

            if existe_funcionario:
                serializer = FuncionarioSerializer(existe_funcionario, many=False)
                existe_funcionario.delete()
                return JsonResponse({"objeto" : serializer.data})

        return JsonResponse({"mensagem": 'usuario não encontrado'})

    if request.method == 'PUT':
        data = json.loads(request.body)
        email = query_params.get('email')

        email_existe = Funcionario.objects.filter(email=data.get('email')).count()
        if email_existe:
            return JsonResponse({'mensagem': 'usuario já existe'})

        funcionario = Funcionario.objects.filter(email=email).first()
        if funcionario:
            funcionario.ano_nascimento = data.get('ano_nascimento')
            funcionario.nome = data.get('nome')
            funcionario.sobrenome = data.get('sobrenome')
            funcionario.email = data.get('email')
            funcionario.funcao = data.get ('funcao')
            funcionario.save()
            serializer = FuncionarioSerializer(funcionario, many=False)
            return JsonResponse(serializer.data)

        return JsonResponse({"mensagem": 'usuario não encontrado'})    

    return JsonResponse({"mensagem": "metodo invalido"})         


def perfil_info(request):
    """View da model Perfil."""

    query_params = request.GET

    if request.method == 'GET':
        lista_perfis = Perfil.objects.all().values()
        serializer = PerfilSerializer(lista_perfis, many=True)

        return JsonResponse({'Perfil': serializer.data})

    if request.method == 'POST':
        data = json.loads(request.body)

        perfil = perfil()
        perfil.nome = data.get('nome')
        perfil.sobrenome = data.get('sobrenome')
        perfil.avatar = data.get('avatar')
        perfil.email = data.get('email')
        perfil.perfil = data.get('perfil')
        perfil.github = data.get('github')
        perfil.celular = data.get('celular')

        existe_perfil = Perfil.objects.filter(email=perfil.email).count()
        if existe_perfil:
           return JsonResponse({'mensagem': 'o usuario já existe'})

        perfil.save()
        serializer = PerfilSerializer(Perfil, many=False)
        return JsonResponse({'objeto': serializer.data})   


    if request.method == 'PUT':
       data = json.loads(request.body) 
       existe_perfil = Perfil.objects.filter(email=query_params.get('email')).count()

       if existe_perfil:
          perfil.nome = data.get('nome')
          perfil.sobrenome = data.get('sobrenome')
          perfil.avatar = data.get('avatar')
          perfil.email = data.get('email')
          perfil.perfil = data.get('perfil')
          perfil.github = data.get('github')
          perfil.celular = data.get('celular')

          perfil.save()
          serializer = PerfilSerializer(Perfil, many=False)
          return JsonResponse({'objeto': serializer.data})

    return JsonResponse({'mensagem': 'email nao existe'})   


    if request.method == 'DELETE':
        existe_email -query-params.get('email')

        perfil = perfil.object.filter(email=existe_email).first()

        if perfil:
           Perfil.delete()
           return JsonResponse({'mensagem': 'objeto deletado'})

           return JsonResponse({'mensagem': 'objeto nao encontrado'})




def curriculo_info(request):
    """View da model Perfil."""

    query_params = request.GET

    if request.method == 'GET':
        return JsonResponse({'mensagem': 'curriculo OK'})

    if request.method == 'POST':
        data = json.loads(request.body)

    if request.method == 'PUT':
       data = json.loads(request.body) 

    if request.method == 'DELETE':
       data = json.loads(request.body)    
        






























    return JsonResponse({"mensagem": "Método inválido"})

























    
