# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RESTafari', '0005_auto_20151111_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fb_uid',
            field=models.CharField(db_index=True, max_length=16),
        ),
    ]
