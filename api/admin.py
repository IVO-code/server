from django.contrib import admin

from .models import Atendimento, Card, Ocupacao, Paciente, Preceptor, Resposta, Roteiro


@admin.register(Preceptor)
class PreceptorAdmin(admin.ModelAdmin):
    list_display = [
        'ativo',
        'login',
        'senha',
        'nome',
    ]


@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = [
        'nome'
    ]


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = [
        'ativo',
        'nome',
    ]


@admin.register(Roteiro)
class RoteiroAdmin(admin.ModelAdmin):
    list_display = [
        'ativo',
        'titulo',
        'descricao',
        'preceptor',
    ]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = [
        'ativo',
        'texto',
        'figura',
        'libras',
        'audioDescricao',
        'titulo',
        'roteiro',
    ]

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = [
        'ativo',
        'texto',
        'figura',
        'libras',
        'audioDescricao',
        'descricao',
        'card',
    ]

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = [
        'preceptor',
        'paciente',
        'roteiro',
    ]
