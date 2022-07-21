from rest_framework import serializers

from .models import Atendimento, Card, Paciente, Preceptor, Roteiro, ElementoComunicativo


class AutenticacaoSerializer(serializers.Serializer):
    usuario = serializers.CharField()
    email = serializers.EmailField()
    senha = serializers.CharField()


class PreceptorSerializer(serializers.ModelSerializer):

    elementos_comunicativos = serializers.SerializerMethodField()

    class Meta:
        model = Preceptor
        fields = [
            'id',
            'ocupacao',
            'username',
            'avatar',
            'email',
            'password',
            'elementos_comunicativos'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_elementos_comunicativos(self, obj):
        elementos_preceptor = []
        elementos = ElementoComunicativo.objects.filter(preceptor_id=obj.id)
        for elemento in elementos:
            elementos_preceptor.append(f'http://locahost:8000/api/elementos/{elemento.id}/')
        return elementos_preceptor


class ElementoComunicativoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElementoComunicativo
        fields = [
            'id',
            'preceptor',
            'ativo',
            'texto',
            'figura',
            'libras',
            'audioDescricao',
            'data',
            'tipo'
        ]


class CardSerializer(serializers.ModelSerializer):

    titulo = serializers.SerializerMethodField()

    descricao = serializers.SerializerMethodField()

    opcoes = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = [
            'id',
            'ativo',
            'data',
            'titulo',
            'descricao',
            'opcoes'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'ativo': {'read_only': True},
            'data': {'read_only': True}
        }

    def get_titulo(self, obj):
        elemento = ElementoComunicativo.objects.filter(id=obj.titulo_id).first()
        return f'http://127.0.0.1:8000/api/elementos/{elemento.id}/'

    def get_descricao(self, obj):
        elemento = ElementoComunicativo.objects.filter(id=obj.descricao_id).first()
        return f'http://127.0.0.1:8000/api/elementos/{elemento.id}/'

    def get_opcoes(self, obj):
        final_opcoes = []
        opcoes = ElementoComunicativo.objects.filter(card_opcao__id=obj.id)
        for opcao in opcoes:
            final_opcoes.append(f'http://127.0.0.1:8000/api/elementos/{opcao.id}/')
        return final_opcoes


class RoteiroSerializer(serializers.ModelSerializer):

    titulo = serializers.SerializerMethodField()

    descricao = serializers.SerializerMethodField()

    cards = serializers.SerializerMethodField()

    class Meta:
        model = Roteiro
        fields = [
            'id',
            'ativo',
            'titulo',
            'data',
            'descricao',
            'cards'
        ]

    def get_titulo(self, obj):
        elemento = ElementoComunicativo.objects.filter(id=obj.titulo_id).first()
        return f'http://127.0.0.1:8000/api/elementos/{elemento.id}/'

    def get_descricao(self, obj):
        elemento = ElementoComunicativo.objects.filter(id=obj.descricao_id).first()
        return f'http://127.0.0.1:8000/api/elementos/{elemento.id}/'

    def get_cards(self, obj):
        final_cards = []
        cards = Card.objects.filter(roteiro_cards__id=obj.id)
        for card in cards:
            final_cards.append(f'http://127.0.0.1:8000/api/elementos/{card.id}/')
        return final_cards


class PacienteSerializer(serializers.ModelSerializer):

    atendimentos = serializers.SerializerMethodField()

    class Meta:
        model = Paciente
        fields = [
            'id',
            'ativo',
            'nome',
            'atendimentos'
        ]

    def get_atendimentos(self, obj):
        elemento = ElementoComunicativo.objects.filter(id=obj.titulo_id).first()
        return f'http://127.0.0.1:8000/api/elementos/{elemento.id}/'


class AtendimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atendimento
        fields = [
            'id',
            'texto',
            'data',
            'paciente',
            'card',
            'opcao'
        ]
