# Generated by Django 5.1.1 on 2024-11-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='id_empleado',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
