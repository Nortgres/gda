# Generated by Django 4.2.4 on 2023-08-27 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_comment_comment_alter_comment_postcomm_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
