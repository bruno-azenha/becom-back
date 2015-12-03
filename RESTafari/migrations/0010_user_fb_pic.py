# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RESTafari', '0009_auto_20151111_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fb_pic',
            field=models.ForeignKey(to='RESTafari.Picture', null=True),
        ),
    ]
