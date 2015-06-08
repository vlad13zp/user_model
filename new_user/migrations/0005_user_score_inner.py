# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0004_auto_20150605_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score_inner',
            field=models.IntegerField(null=True),
        ),
    ]
