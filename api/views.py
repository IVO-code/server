from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
"""
from api.serializers import PreceptorSerializer

from .models import Atendimento, Card, Paciente, Preceptor, Roteiro


@api_view(['GET', 'POST'])
def preceptores_CR(self, request, format=None):
    if request.method == 'GET':
        preceptores = Preceptor.objects.all()
        serializer = PreceptorSerializer(preceptores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PreceptorSerializer(data=request.data)
        if serializer.is_valid(reaise_exeption=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def preceptores_RUD(self, request, preceptor_pk=None, format=None):
    try:
        preceptor = Preceptor.objects.get(pk=preceptor_pk)
    except preceptor.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = PreceptorSerializer(data=preceptor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PreceptorSerializer(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        preceptor.delete()
        return Response(status=status.HTTP_200_OKs)
"""
