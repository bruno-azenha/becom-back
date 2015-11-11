# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RESTafari', '0004_auto_20151110_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fb_token',
            field=models.CharField(max_length=64, default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='fb_uid',
            field=models.CharField(unique=True, db_index=True, max_length=16, default=-1),
            preserve_default=False,
        ),
    ]
