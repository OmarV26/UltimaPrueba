# Generated by Django 5.0.1 on 2024-12-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservasAPP', '0003_alter_reservas_estadoreserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
