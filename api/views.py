from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets


from .models import Atendimento, Card, ElementoComunicativo, Paciente, Preceptor, Roteiro
from .serializers import PreceptorSerializer, CardSerializer, RoteiroSerializer, AtendimentoSerializer, ElementoComunicativoSerializer, PacienteSerializer, AutenticacaoSerializer

@api_view(['POST'])
def login(request, format=None):

    if request.method == 'POST':
        login = AutenticacaoSerializer(request.data)
        Usuarioresultado = authenticate(username=login.data['usuario'], password=login.data['senha'])
        if Usuarioresultado is not None:
            token = Token.objects.get_or_create(user=Usuarioresultado)
            return Response({"token": token[0].key}, status=status.HTTP_202_ACCEPTED)
        else: return Response({"erro": "erro de usuario ou senha"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else: return Response(status=status.HTTP_400_BAD_REQUEST)


class PreceptorViewSet(viewsets.ModelViewSet):
    queryset = Preceptor.objects.all()
    serializer_class = PreceptorSerializer
    
    
class ElementoComunicativoViewSet(viewsets.ModelViewSet):
    queryset = ElementoComunicativo.objects.all()
    serializer_class = ElementoComunicativoSerializer

