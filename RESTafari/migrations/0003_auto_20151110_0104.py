# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RESTafari', '0002_auto_20151109_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('reach', models.FloatField(default=20.0)),
                ('id_picture', models.ForeignKey(null=True, to='RESTafari.Picture')),
                ('id_text', models.ForeignKey(null=True, to='RESTafari.Text')),
                ('id_video', models.ForeignKey(null=True, to='RESTafari.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('beacon', models.ForeignKey(to='RESTafari.Beacon')),
                ('text', models.ForeignKey(to='RESTafari.Text')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='beacom',
            name='id_picture',
        ),
        migrations.RemoveField(
            model_name='beacom',
            name='id_text',
        ),
        migrations.RemoveField(
            model_name='beacom',
            name='id_video',
        ),
        migrations.RemoveField(
            model_name='beacom',
            name='user',
        ),
        migrations.DeleteModel(
            name='Beacom',
        ),
        migrations.AddField(
            model_name='beacon',
            name='user',
            field=models.ForeignKey(to='RESTafari.User'),
        ),
    ]
