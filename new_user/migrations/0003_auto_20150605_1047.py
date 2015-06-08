# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0002_auto_20150605_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatereg',
            name='name',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
