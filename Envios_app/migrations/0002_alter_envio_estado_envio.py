# Generated by Django 5.1.1 on 2024-11-27 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Envios_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='estado_envio',
            field=models.CharField(max_length=100),
        ),
    ]
