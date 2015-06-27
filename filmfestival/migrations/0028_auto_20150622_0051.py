# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import filmfestival.models


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0027_auto_20150621_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', sorl.thumbnail.fields.ImageField(max_length=256, upload_to=filmfestival.models.location_image_path, blank=True)),
                ('address', models.TextField(default=b'', blank=True)),
                ('url', models.URLField(default=b'', blank=True)),
                ('embeded_map', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='screening',
            name='day',
            field=models.ForeignKey(blank=True, to='filmfestival.Day', null=None),
        ),
        migrations.AddField(
            model_name='screening',
            name='location',
            field=models.ForeignKey(blank=True, to='filmfestival.Location', null=True),
        ),
    ]
