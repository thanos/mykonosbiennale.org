# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filmfestival.models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=200)),
                ('info', models.TextField(default=b'')),
                ('file', models.FileField(max_length=256, upload_to=filmfestival.models.document_path, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('dir_by', models.CharField(max_length=128)),
                ('sub_by', models.CharField(default=b'', max_length=128)),
                ('subtitles', models.BooleanField(default=False)),
                ('language', models.CharField(max_length=128)),
                ('actors', models.TextField()),
                ('year', models.CharField(max_length=4)),
                ('runtime', models.IntegerField()),
                ('country', models.TextField()),
                ('log_line', models.TextField(default=b'')),
                ('synopsis', models.TextField(default=b'')),
                ('synopsis_125', models.TextField(default=b'')),
                ('synopsis_250', models.TextField(default=b'')),
                ('first_time', models.CharField(default=b'', max_length=64, blank=True)),
                ('twitter', models.CharField(default=b'', max_length=64, blank=True)),
                ('facebook', models.CharField(default=b'', max_length=64, blank=True)),
                ('other_social_media', models.CharField(default=b'', max_length=64, blank=True)),
                ('directors', models.TextField(default=b'')),
                ('screenwriters', models.TextField(default=b'')),
                ('producers', models.TextField(default=b'')),
                ('exec_producers', models.TextField(default=b'')),
                ('co_producers', models.TextField(default=b'')),
                ('cinematographers', models.TextField(default=b'')),
                ('product_designers', models.TextField(default=b'')),
                ('art_directors', models.TextField(default=b'')),
                ('editors', models.TextField(default=b'')),
                ('sound_editors', models.TextField(default=b'')),
                ('composers', models.TextField(default=b'')),
                ('screenings', models.TextField(default=b'')),
                ('status', models.CharField(default=b'', max_length=64, blank=True)),
                ('url', models.URLField(default=b'', blank=True)),
                ('genres', models.CharField(default=b'', max_length=128, blank=True)),
                ('niches', models.CharField(default=b'', max_length=256, blank=True)),
                ('info', models.TextField(default=b'', blank=True)),
                ('directors_statement', models.TextField(default=b'', blank=True)),
                ('production_notes', models.TextField(default=b'', blank=True)),
                ('film_type', models.CharField(default=b'Dramatic Nights', max_length=30, choices=[(b'Dramatic Nights', b'Dramatic Nights'), (b'Video Grafitti', b'Video Grafitti'), (b'Dance', b'Dance'), (b'Documentary', b'Dance')])),
                ('poster', models.ImageField(max_length=256, upload_to=filmfestival.models.poster_path, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('what', models.CharField(max_length=128)),
                ('email', models.EmailField(default=b'', max_length=254, blank=True)),
                ('country', django_countries.fields.CountryField(default=b'', max_length=2, blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default=b'', max_length=128, blank=True)),
                ('headshot', models.ImageField(max_length=256, upload_to=filmfestival.models.headshot_path, blank=True)),
                ('film', models.ForeignKey(to='filmfestival.Film')),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=200)),
                ('info', models.TextField(default=b'')),
                ('image', models.ImageField(max_length=256, upload_to=filmfestival.models.screenshot_path, blank=True)),
                ('film', models.ForeignKey(related_name='filmfestival_screenshot_related', to='filmfestival.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Still',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=200)),
                ('info', models.TextField(default=b'')),
                ('image', models.ImageField(max_length=256, upload_to=filmfestival.models.still_path, blank=True)),
                ('film', models.ForeignKey(related_name='filmfestival_still_related', to='filmfestival.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='documentation',
            name='film',
            field=models.ForeignKey(related_name='filmfestival_documentation_related', to='filmfestival.Film'),
        ),
    ]
