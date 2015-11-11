# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RESTafari', '0007_auto_20151111_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
