# Generated by Django 4.2.4 on 2023-09-28 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0009_security'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='security',
            options={'ordering': ('name', 'second_name'), 'verbose_name': 'Сотрудник службы безопасности', 'verbose_name_plural': 'Сотрудники службы безопасности'},
        ),
        migrations.AddField(
            model_name='security',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
