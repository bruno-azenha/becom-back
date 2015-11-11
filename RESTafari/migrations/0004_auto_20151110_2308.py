# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RESTafari', '0003_auto_20151110_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326),
        ),
    ]
