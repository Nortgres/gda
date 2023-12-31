# Generated by Django 4.2.4 on 2023-08-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_flight_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('flights', models.ManyToManyField(related_name='passenger_flights', to='flights.flight', verbose_name='Вылеты')),
            ],
        ),
    ]
