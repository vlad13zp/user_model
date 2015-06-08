# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0006_auto_20150605_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='score_inner',
        ),
    ]
