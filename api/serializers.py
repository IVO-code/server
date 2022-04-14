from rest_framework import serializers

from .models import Atendimento, Card, Ocupacao, Paciente, Preceptor, Roteiro, Resposta


class OcupacaoSerializer(serializers.ModelSerializer):

    preceptores = serializers.Hyperlink(
        many=True,
        read_only=True,
        view_name='preceptor-detail'
    )

    class Meta:
        model = Ocupacao
        fields = [
            'id',
            'nome',
            'preceptores'
        ]


class PreceptorSerializer(serializers.ModelSerializer):

    roteiros = serializers.Hyperlink(
        many=True,
        read_only=True,
        view_name='roteiro-detail'
    )

    atendimentos = serializers.Hyperlink(
        many=True,
        read_only=True,
        view_name='atendimento-detail'
    )

    class Meta:
        model = Preceptor
        fields = [
            'id',
            'ocupacao',
            'ativo',
            'login',
            'senha',
            'nome',
            'email',
            'roteiros',
            'atendimentos',
        ]
        extra_kargs = {
            'senha': {'write_only': True},
        }


class RoteiroSerializer(serializers.ModelSerializer):

    cards = serializers.Hyperlink(
        many=True,
        read_only=True,
        view_name='card-detail'
    )

    atendimentos = serializers.Hyperlink(
        many=True,
        read_only=True,
        view_name='atendimento-detail'
    )

    class Meta:
        model = Roteiro
        fields = [
            'id'
            'preceptor',
            'ativo',
            'titulo',
            'descricao',
            'cards'
            'atendimentos'
        ]


class CardSerializer(serializers.ModelSerializer):

    respostas = serializers.Hyperlink(
        many=True,
        read_only=True,
        view_name='resposta-detail'
    )

    class Meta:
        model = Card
        fields = [
            'id',
            'roteiro',
            'ativo',
            'texto',
            'figura',
            'libras',
            'audioDescricao',
            'titulo',
            'respostas'
        ]


class RespostaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resposta
        fields = [
            'id',
            'card',
            'ativo',
            'texto',
            'figura',
            'libras',
            'audioDescricao',
            'descricao',
            'escolhida',
        ]


class PacienteSerializer(serializers.ModelSerializer):

    atendimentos = serializers.Hyperlink(
        many=True,
        read_only=True,
        view_name='atendimento-detail'
    )

    class Meta:
        model = Paciente
        fields = [
            'id',
            'ativo',
            'nome',
            'atendimentos'
        ]


class AtendimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atendimento
        fields = [
            'id',
            'ativo',
            'preceptor',
            'paciente',
            'roteiro',
        ]

