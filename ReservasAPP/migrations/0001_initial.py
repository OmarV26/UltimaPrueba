# Generated by Django 5.0.1 on 2024-12-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField()),
                ('hora', models.TimeField()),
                ('cantidadPersonas', models.IntegerField()),
                ('estadoReserva', models.CharField(max_length=100)),
            ],
        ),
    ]
