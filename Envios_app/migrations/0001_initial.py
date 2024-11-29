# Generated by Django 5.1.1 on 2024-11-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id_envio', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('direccion_envio', models.CharField(max_length=100)),
                ('compania_envio', models.CharField(max_length=100)),
                ('fecha_envio', models.DateField()),
                ('estado_envio', models.BooleanField()),
                ('fecha_llegada', models.DateField()),
            ],
        ),
    ]