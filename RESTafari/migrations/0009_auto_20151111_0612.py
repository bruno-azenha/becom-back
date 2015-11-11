# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RESTafari', '0008_auto_20151111_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='id',
            field=models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID'),
        ),
    ]
