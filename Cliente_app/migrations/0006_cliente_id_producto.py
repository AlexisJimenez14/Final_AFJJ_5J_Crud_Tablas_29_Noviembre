# Generated by Django 5.1.1 on 2024-11-29 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente_app', '0005_alter_cliente_id_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='id_producto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
