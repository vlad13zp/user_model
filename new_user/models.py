# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False


class User(AbstractUser):
    avatar = models.ImageField(
        _(u'avatar'), upload_to='photos/%Y/%m/%d',
        blank=True, max_length=1000)
    birthday = models.DateField(_(u'birthday'), blank=True, null=True)


class DateUser(models.Model):
    username = models.CharField(max_length=300)
    date_time = models.DateTimeField(null=True)

    def __unicode__(self):
        return 'New user : {0}'.format(self.username)
