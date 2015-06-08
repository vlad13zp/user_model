# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0005_user_score_inner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='score_inner',
            field=models.IntegerField(null=True, verbose_name='score'),
        ),
    ]
