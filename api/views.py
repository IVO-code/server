from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status

from .models import Atendimento, Card, ElementoComunicativo, Paciente, Preceptor, Roteiro
from .serializers import PreceptorSerializer, CardSerializer, RoteiroSerializer, AtendimentoSerializer, ElementoComunicativoSerializer, PacienteSerializer, AutenticacaoSerializer
from .permissions import UserLoginPermission

@api_view(['POST'])
@permission_classes([UserLoginPermission])
def login(request, format=None):

    if request.method == 'POST':
        login = AutenticacaoSerializer(request.data)
        resultado = Preceptor.objects.filter(username=login.data['usuario']).filter(password=login.data['senha'])
        if len(resultado) == 1:
           token = Token.objects.get(user_id=resultado[0].id)
           return Response({"token": token.key}, status=status.HTTP_202_ACCEPTED)
        else: return Response({"erro": "erro de usuario ou senha"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else: return Response(status=status.HTTP_400_BAD_REQUEST)


class PreceptorViewSet(viewsets.ModelViewSet):
    queryset = Preceptor.objects.all()
    serializer_class = PreceptorSerializer
    

class ElementoComunicativoViewSet(viewsets.ModelViewSet):
    queryset = ElementoComunicativo.objects.all()
    serializer_class = ElementoComunicativoSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class RoteiroViewSet(viewsets.ModelViewSet):
    queryset = Roteiro.objects.all()
    serializer_class = RoteiroSerializer


class AtendimentoViewSet(viewsets.ModelViewSet):
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
