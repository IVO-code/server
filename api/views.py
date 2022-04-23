from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Atendimento, Card, Paciente, Preceptor, Roteiro
from .serializers import PreceptorSerializer, CardSerializer, RoteiroSerializer, AtendimentoSerializer, ElementoComunicativoSerializer, PacienteSerializer, AutenticacaoSerializer

@api_view(['POST'])
def login(request, format=None):

    if request.method == 'POST':
        login = AutenticacaoSerializer(request.data)
        Usuarioresultado = authenticate(username=login.data['usuario'], password=login.data['senha'])
        if Usuarioresultado is not None:
            token = Token.objects.get_or_create(user=Usuarioresultado)
            return Response({"token": token[0].key}, status=status.HTTP_202_ACCEPTED)
        else: return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    else: return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def preceptor_CR(request, format=None):

    if request.method == 'GET':
        preceptores = Preceptor.objects.all()
        serilizer = PreceptorSerializer(preceptores, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PreceptorSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    else: Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def preceptor_RUD(request, preceptor_pk, format=None):
    try:
        preceptor = Preceptor.objects.get(pk=preceptor_pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = PreceptorSerializer(preceptor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PreceptorSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        preceptor.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)


