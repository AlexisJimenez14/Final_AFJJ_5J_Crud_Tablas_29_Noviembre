# Generated by Django 5.1.1 on 2024-11-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente_app', '0002_rename_direrccion_cliente_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_cliente',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]