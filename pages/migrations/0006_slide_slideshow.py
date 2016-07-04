# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150519_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(default=b'', max_length=128, blank=True)),
                ('slug', models.SlugField(max_length=200)),
                ('content', models.TextField(default=b'', blank=True)),
                ('css', models.TextField(default=b'')),
                ('visible', models.BooleanField(default=True)),
                ('image', models.ImageField(max_length=256, upload_to=pages.models.poster_path, blank=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=128, blank=True)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
