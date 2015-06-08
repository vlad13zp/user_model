# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0003_auto_20150605_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdatereg',
            name='name',
        ),
        migrations.DeleteModel(
            name='UserDateReg',
        ),
    ]
