# Generated by Django 4.2.4 on 2023-08-28 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_rename_comment_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания'),
        ),
    ]
