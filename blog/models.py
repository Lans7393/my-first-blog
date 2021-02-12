from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    '''
    Posts (articles) created by users
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

class Comment(models.Model):
    '''
    Comments under the posts
    '''
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    author = models.CharField('автор коментария', max_length=200)
    text = models.TextField('текст коментария')
    created_date = models.DateTimeField('дата создания', default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text
        
    def approve(self):
        self.approved_comment = True
        self.save()

    class Meta:
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'

    
