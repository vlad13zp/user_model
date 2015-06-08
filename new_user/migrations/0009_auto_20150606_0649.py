# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0008_dateuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateuser',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
