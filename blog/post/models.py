from django.db import models


# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=200, verbose_name='Тема поста')
    posttext = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'subject: {self.postname} text: {self.posttext} '


class Comment(models.Model):
    postcomm = models.ForeignKey(Post, verbose_name='Комментируемый пост', related_name='comment_postcomment',
                                 on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=200, verbose_name='Комментарий')

    def __str__(self):
        return f'Комментарий: {self.comment} к посту {self.postcomm} '
