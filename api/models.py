from django.db import models

from django.contrib.auth.models import AbstractUser


class Preceptor(AbstractUser):
    ocupacao = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'preceptor'
        verbose_name_plural = 'preceptores'

    def __str__(self):
        return f'{self.username}'


class ElementoComunicativo(models.Model):
    ativo = models.BooleanField(default=True)
    texto = models.CharField(max_length=255)
    figura = models.URLField()
    libras = models.URLField()
    audioDescricao = models.URLField()
    data = models.DateTimeField(auto_now_add=True)

    preceptor = models.ForeignKey(
        Preceptor,
        related_name='elemento_preceptor',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'elemento'
        verbose_name_plural = 'elemento'

    def __str__(self):
        return f'{self.texto}'


class Card(models.Model):
    ativo = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    titulo = models.ForeignKey(
        ElementoComunicativo,
        related_name='card_titulo_elemento',
        on_delete=models.DO_NOTHING
    )

    descricao = models.ForeignKey(
        ElementoComunicativo,
        related_name='card_descricao_elemento',
        on_delete=models.DO_NOTHING
    )

    opcoes = models.ManyToManyField(ElementoComunicativo)

    class Meta:
        ordering = ['id']
        verbose_name = 'card'
        verbose_name_plural = 'cards'

    def __str__(self):
        return f'{self.titulo.texto}'


class Roteiro(models.Model):
    ativo = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    titulo = models.ForeignKey(
        ElementoComunicativo,
        related_name='roteiro_titulo_elemento',
        on_delete=models.DO_NOTHING
    )

    descricao = models.ForeignKey(
        ElementoComunicativo,
        related_name='roteiro_descricao_elemento',
        on_delete=models.DO_NOTHING
    )

    cards = models.ManyToManyField(
        Card
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'roteiro'
        verbose_name_plural = 'roteiros'

    def __str__(self):
        return f'{self.titulo.texto}'


class Paciente(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField(blank=False, max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'

    def __str__(self):
        return f'{self.nome}'


class Atendimento(models.Model):
    ativo = models.BooleanField(default=True)
    texto = models.CharField(blank=False, max_length=255)
    data = models.DateTimeField(auto_now_add=True)

    paciente = models.ManyToManyField(Paciente)

    card = models.ManyToManyField(Card)

    opcao = models.ManyToManyField(ElementoComunicativo)

    class Meta:
        ordering = ['id']
        verbose_name = 'atendimento'
        verbose_name_plural = 'atendimento'

    def __str__(self):
        return f'{self.texto} - {self.paciente.nome}'
