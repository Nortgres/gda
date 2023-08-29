# Generated by Django 4.2.4 on 2023-08-17 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_remove_flight_destination_remove_flight_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flight_destination', to='flights.airport', verbose_name='Точка прибытия'),
        ),
        migrations.AddField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flight_origin', to='flights.airport', verbose_name='Точка отправления'),
        ),
    ]