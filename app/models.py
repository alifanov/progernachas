# coding: utf-8
from django.db import models

# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=256, verbose_name=u'Имя')
    email = models.EmailField(verbose_name=u'Email')

    def __unicode__(self):
        return u'{} {}'.format(self.name, self.email)

    class Meta:
        verbose_name = u'Подписчик'
        verbose_name_plural = u'Подписчики'