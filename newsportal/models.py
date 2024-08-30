from django.db import models
from django.contrib.auth.models import User
#from django.db.models import Sum
#from django.db.models.functions import Coalesce
from django.urls import reverse
from django.core.cache import cache
from django.contrib.postgres.fields import ArrayField
#from django_resized import ResizedImageField



class Post(models.Model): 
    Tank = 'TK'
    Hil = 'AR'
    DD = 'DD'
    Torgovci = 'TC'
    GildMaster = 'GD'
    CvestGiver = 'CG'
    Kuznec = 'KZ'
    Kojevnik = 'KJ'
    Zelevar = 'ZV'
    MasterZakinanii = 'MZ'
    CATEGORY_CHOICES = (
        (Tank, 'Танк'),
        (Hil, 'Хил'),
        (DD, 'ДД'),
        (Torgovci, 'Торговец'),
        (GildMaster, 'Гилдмастер'),
        (CvestGiver, 'Квестгивер'),
        (Kuznec, 'Кузнец'),
        (Kojevnik, 'Кожевник'),
        (Zelevar, 'Зельевар'),
        (MasterZakinanii, 'Мастер Заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    nameCat = models.CharField(max_length=64, unique=False, choices=CATEGORY_CHOICES, verbose_name='Category', default='Tanks')
    title = models.CharField(max_length=128)
    text = models.TextField()
    files = models.FileField(upload_to='uploads/', blank=True)
    dateMsg = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse('post_list')


    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = 'Публикации'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')

class Comment(models.Model):
    author = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, unique=False, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)
    dateComm = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.author}:{self.post}:{self.text[:10]}'

    def get_absolute_url(self):
        return reverse('Comments', args=[str(self.post.id)])