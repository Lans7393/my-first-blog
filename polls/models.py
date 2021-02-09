import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('Вопрос', max_length=200)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Вариант ответа', max_length=200)
    votes = models.IntegerField('Количество голосов', default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently():
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
