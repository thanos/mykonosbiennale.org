# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pages.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('festival', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('templates', models.CharField(default=b'page.html', max_length=128)),
                ('description_155', models.TextField(default=b'', blank=True)),
                ('description_200', models.TextField(default=b'', blank=True)),
                ('description_300', models.TextField(default=b'', blank=True)),
                ('image', models.ImageField(max_length=256, upload_to=pages.models.poster_path, blank=True)),
                ('url', models.URLField(default=b'', blank=True)),
                ('visibile', models.BooleanField(default=True)),
                ('css', models.TextField(default=b'')),
                ('javascript', models.TextField(default=b'')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=128, blank=True)),
                ('slug', models.SlugField(max_length=200)),
                ('content', models.TextField(default=b'', blank=True)),
                ('css', models.TextField(default=b'')),
                ('page', models.ForeignKey(to='pages.Page')),
            ],
        ),
    ]
