# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('reach', models.FloatField(default=20.0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('beacon', models.ForeignKey(to='RESTafari.Beacon')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('picture', models.FileField(upload_to='user_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('video', models.FileField(upload_to='user_vid')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.ForeignKey(to='RESTafari.Text'),
        ),
        migrations.AddField(
            model_name='beacon',
            name='id_picture',
            field=models.ForeignKey(to='RESTafari.Picture', null=True),
        ),
        migrations.AddField(
            model_name='beacon',
            name='id_text',
            field=models.ForeignKey(to='RESTafari.Text', null=True),
        ),
        migrations.AddField(
            model_name='beacon',
            name='id_video',
            field=models.ForeignKey(to='RESTafari.Video', null=True),
        ),
        migrations.AddField(
            model_name='beacon',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
