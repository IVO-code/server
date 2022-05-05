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
            elementos_preceptor.append(f'http://127.0.0.1:8000/api/elementos/{elemento.id}/')
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
            'data'
        ]


class CardSerializer(serializers.ModelSerializer):

    titulo = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='elemento-detail'
    )

    descricao = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='elemento-detail'
    )

    opcoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='elemento-detail'
    )

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


class RoteiroSerializer(serializers.ModelSerializer):

    titulo = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='elemento-detail'
    )

    descricao = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='elemento-detail'
    )

    cards = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='card-detail'
    )

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


class PacienteSerializer(serializers.ModelSerializer):

    atendimentos = serializers.HyperlinkedRelatedField(
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
            'texto',
            'data',
            'paciente',
            'card',
            'opcao'
        ]



