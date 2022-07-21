from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status

import cloudinary
import cloudinary.uploader
import cloudinary.api

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
           return Response({"token": token.key, "id": resultado[0].id}, status=status.HTTP_202_ACCEPTED)
        else: return Response({"erro": "erro de usuario ou senha"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else: return Response(status=status.HTTP_400_BAD_REQUEST)


class PreceptorViewSet(viewsets.ModelViewSet):
    queryset = Preceptor.objects.all()
    serializer_class = PreceptorSerializer

    @action(detail=True, methods=["post"], url_path='upload_avatar')
    def upload_avatar(self, request, pk=None):
        user = Preceptor.objects.filter(id=pk).get()
        avatar = request.data.get('picture')
        upload_data = cloudinary.uploader.upload(avatar)
        user.avatar = upload_data['url']
        user.save()
        return Response(status=status.HTTP_200_OK)
    

class ElementoComunicativoViewSet(viewsets.ModelViewSet):
    queryset = ElementoComunicativo.objects.all()
    serializer_class = ElementoComunicativoSerializer

    @action(detail=True, methods=["post"], url_path='upload_figure')
    def upload_figure(self, request, pk=None):
        elemento = ElementoComunicativo.objects.filter(id=pk).get()
        avatar = request.data.get('picture')
        upload_data = cloudinary.uploader.upload(avatar)
        elemento.figura = upload_data['url']
        elemento.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], url_path='type')
    def get_by_type(self, request, tipo=None):
        elementos = ElementoComunicativo.objects.filter(tipo=tipo)
        return elementos


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request):
        card = Card.objects.create()
        card.titulo = ElementoComunicativo.objects.get(id=request.data['titulo'])
        card.descricao = ElementoComunicativo.objects.get(id=request.data['descricao'])
        card.opcoes.set(ElementoComunicativo.objects.filter(pk__in=request.data['opcoes']))
        card.save()


class RoteiroViewSet(viewsets.ModelViewSet):
    queryset = Roteiro.objects.all()
    serializer_class = RoteiroSerializer


class AtendimentoViewSet(viewsets.ModelViewSet):
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
