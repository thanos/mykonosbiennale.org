# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import festivalA.models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0004_auto_20151013_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('statement', models.TextField(default=b'')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', sorl.thumbnail.fields.ImageField(max_length=256, upload_to=festivalA.models.location_image_path, blank=True)),
                ('address', models.TextField(default=b'', blank=True)),
                ('url', models.URLField(default=b'', blank=True)),
                ('embeded_map', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='headshot',
            field=models.ImageField(max_length=256, upload_to=festivalA.models.participant_name, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='directed_by',
            field=models.ManyToManyField(related_name='films_directed', to='festivalA.Director'),
        ),
    ]
