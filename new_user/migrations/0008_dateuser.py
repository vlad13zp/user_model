# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0007_remove_user_score_inner'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=300)),
                ('date_time', models.DateField(null=True)),
            ],
        ),
    ]
