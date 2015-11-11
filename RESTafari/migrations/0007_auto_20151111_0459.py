# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RESTafari', '0006_auto_20151111_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fb_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='fb_uid',
            field=models.CharField(db_index=True, unique=True, max_length=16),
        ),
    ]
