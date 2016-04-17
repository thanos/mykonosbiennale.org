# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
import festival.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=128, blank=True)),
                ('slug', models.SlugField(max_length=128)),
                ('description', models.TextField(default=b'', blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('image', models.ImageField(max_length=256, upload_to=festival.models.artNamer, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('template', models.CharField(default=b'2015-artist.html', max_length=128)),
                ('bio', models.TextField(default=b'', blank=True)),
                ('statement', models.TextField(default=b'', blank=True)),
                ('email', models.EmailField(default=b'', max_length=254, blank=True)),
                ('country', django_countries.fields.CountryField(default=b'', max_length=2, blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default=b'', max_length=128, blank=True)),
                ('headshot', models.ImageField(max_length=256, upload_to=festival.models.headshotNamer, blank=True)),
                ('homepage', models.URLField(default=b'', blank=True)),
                ('poster', models.ImageField(max_length=256, upload_to=festival.models.posterNamer, blank=True)),
                ('visible', models.BooleanField(default=True)),
                ('css', models.TextField(default=b'')),
                ('javascript', models.TextField(default=b'')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
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
        migrations.AddField(
            model_name='artist',
            name='festival',
            field=models.ForeignKey(to='festival.Festival'),
        ),
        migrations.AddField(
            model_name='art',
            name='artist',
            field=models.ForeignKey(to='festival.Artist'),
        ),
    ]
