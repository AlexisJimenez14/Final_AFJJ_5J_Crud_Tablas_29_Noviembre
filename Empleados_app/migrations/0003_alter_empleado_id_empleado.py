# Generated by Django 5.1.1 on 2024-11-29 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados_app', '0002_alter_empleado_id_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='id_empleado',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]