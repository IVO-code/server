# Generated by Django 2.2.9 on 2022-05-08 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220505_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='opcao',
            field=models.ManyToManyField(related_name='atendimento_opcao', to='api.ElementoComunicativo'),
        ),
        migrations.AlterField(
            model_name='card',
            name='opcoes',
            field=models.ManyToManyField(related_name='card_opcao', to='api.ElementoComunicativo'),
        ),
        migrations.AlterField(
            model_name='roteiro',
            name='cards',
            field=models.ManyToManyField(related_name='roteiro_cards', to='api.Card'),
        ),
    ]
