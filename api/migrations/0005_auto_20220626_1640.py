# Generated by Django 2.2.9 on 2022-06-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_preceptor_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preceptor',
            name='avatar',
            field=models.ImageField(null=True, upload_to='preceptor_avatar'),
        ),
    ]
