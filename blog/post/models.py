from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=30, verbose_name='Тема поста')
    posttext = models.CharField(max_length=500, verbose_name='Текст')

    def __str__(self):
        return f'#Тема: {self.postname} #Текст: {self.posttext}'