# Generated by Django 5.1.1 on 2024-11-29 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Promocion_app', '0003_alter_promocion_id_promocion'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='id_producto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
