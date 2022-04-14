from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Modelo de usuario do sistema
class Usuario(models.Model):
    ativo = models.BooleanField(default=True)
    login = models.CharField(blank=False, max_length=255)
    senha = models.CharField(blank=False, max_length=255)

    class Meta:
        abstract = True

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


# Tipo de função do funcionario dentro da instiuição
class Ocupacao(models.Model):
    nome = models.CharField(blank=False, max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'ocupacao'
        verbose_name_plural = 'ocupacaoes'


# Pessoa responsavel pela comunicação
class Preceptor(Usuario):
    nome = models.CharField(blank=False, max_length=255)
    ocupacao = models.ForeignKey(
        Ocupacao,
        related_name='ocupacaoes_preceptor',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'preceptor'
        verbose_name_plural = 'preceptores'
        unique_together = ['id', 'ocupacao']


# Pessoa que irá interagir com o preceptor
class Paciente(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField(blank=False, max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'


# modelo de comunicacao
class ElementoComunicativo(models.Model):
    ativo = models.BooleanField(default=True)
    texto = models.CharField(max_length=255)
    figura = models.URLField()
    libras = models.URLField()
    audioDescricao = models.URLField()

    class Meta:
        abstract = True


# Objeto que vai conter os cards de perguntas
class Roteiro(models.Model):
    ativo = models.BooleanField(default=True)
    titulo = models.CharField(blank=False, max_length=255)
    descricao = models.CharField(blank=False, max_length=255)
    preceptor = models.ForeignKey(
        Preceptor,
        related_name='roteiro_preceptores',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'roteiro'
        verbose_name_plural = 'roteiros'
        unique_together = ['id', 'preceptor']


# card de comunicação ou perguntas
class Card(ElementoComunicativo):
    titulo = models.CharField(blank=False, max_length=255)
    roteiro = models.ForeignKey(
        Roteiro,
        related_name='card_roteiros',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'card'
        verbose_name_plural = 'cards'
        unique_together = ['id', 'roteiro']


# uma lista de respostas dentro de um card
class Resposta(ElementoComunicativo):
    descricao = models.CharField(blank=False, max_length=255)
    card = models.ForeignKey(
        Card,
        related_name='resposta_cards',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'resposta'
        verbose_name_plural = 'respostas'
        unique_together = ['id', 'card']


# um preceptor aplicando um roteiro de comunicação com um paciente
class Atendimento(models.Model):
    preceptor = models.ForeignKey(
        Preceptor,
        related_name='atendimento_preceptores',
        on_delete=models.CASCADE
    )
    paciente = models.ForeignKey(
        Paciente,
        related_name='atendimento_pacientes',
        on_delete=models.CASCADE
    )
    roteiro = models.ForeignKey(
        Roteiro,
        related_name='atendimento_roteiros',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'roteiro'
        verbose_name_plural = 'roteiros'
        unique_together = ['preceptor', 'paciente', 'roteiro']
