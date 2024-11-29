# Generated by Django 5.1.1 on 2024-11-29 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('fecha_produccion', models.IntegerField()),
                ('lote', models.CharField(max_length=100)),
                ('id_proveedor', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
            ],
        ),
    ]