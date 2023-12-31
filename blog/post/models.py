from django.db import models
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=200, verbose_name='Тема поста')
    posttext = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(verbose_name='Время создания', default=now)

    def __str__(self):
        return f'subject: {self.postname} text: {self.posttext}'

    def get_comments(self):
        return self.comment_postcomment.all()


class Comments(models.Model):
    postcomm = models.ForeignKey(Post, verbose_name='Комментируемый пост', related_name='comment_postcomment', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return f'Текст комментария: {self.comment}'
