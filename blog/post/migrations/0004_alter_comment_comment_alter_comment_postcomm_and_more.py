# Generated by Django 4.2.4 on 2023-08-23 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_comment_postcomm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='postcomm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_postcomment', to='post.post', verbose_name='Комментируемый пост'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postname',
            field=models.CharField(max_length=200, verbose_name='Тема поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='posttext',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]