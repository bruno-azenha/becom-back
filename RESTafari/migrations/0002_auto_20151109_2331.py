# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RESTafari', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacom',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('reach', models.FloatField(default=20.0)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('picture', models.FileField(upload_to='user_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('video', models.FileField(upload_to='user_vid')),
            ],
        ),
        migrations.DeleteModel(
            name='HelloClass',
        ),
        migrations.AddField(
            model_name='beacom',
            name='id_picture',
            field=models.ForeignKey(to='RESTafari.Picture', null=True),
        ),
        migrations.AddField(
            model_name='beacom',
            name='id_text',
            field=models.ForeignKey(to='RESTafari.Text', null=True),
        ),
        migrations.AddField(
            model_name='beacom',
            name='id_video',
            field=models.ForeignKey(to='RESTafari.Video', null=True),
        ),
        migrations.AddField(
            model_name='beacom',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
