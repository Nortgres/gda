# Generated by Django 4.2.4 on 2023-08-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, verbose_name='Комментарий')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='posttext',
            field=models.CharField(max_length=500, verbose_name='Текст'),
        ),
    ]
