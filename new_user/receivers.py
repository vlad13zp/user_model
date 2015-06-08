# -*- coding: utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save
from new_user.actions import make_info_user
from new_user.models import User


@receiver(post_save, sender=User)
def add_time(sender, **kwargs):
    make_info_user(kwargs['instance'])
