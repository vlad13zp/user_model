# -*- coding: utf-8 -*-
import datetime
from new_user.models import DateUser


def make_info_user(name):
    DateUser.objects.create(username=name,
                            date_time=datetime.datetime.now())
