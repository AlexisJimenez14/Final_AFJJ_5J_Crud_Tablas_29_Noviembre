# Generated by Django 5.1.1 on 2024-11-29 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores_app', '0003_alter_proveedor_id_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='id_producto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
