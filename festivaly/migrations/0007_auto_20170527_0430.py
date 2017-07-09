# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagulous.models.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festivaly', '0006_participant_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sort_by', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('ref', models.CharField(max_length=30)),
                ('film_source', models.CharField(default=b'withoutabox', max_length=20, choices=[(b'withoutabox', b'withoutabox'), (b'filmfreeway', b'filmfreeway'), (b'other', b'other')])),
                ('tags', tagulous.models.fields.TagField(autocomplete_view=b'festivalA_tag_autocomplete', default=b'', initial=b'2013, 2013/artist, 2015', tree=True, force_lowercase=True, to='festivaly.Tag', blank=True, help_text='Enter a comma-separated tag string', _set_tag_meta=True)),
            ],
            options={
                'ordering': ['ref'],
            },
        ),
        migrations.AlterField(
            model_name='participant',
            name='headshot',
            field=versatileimagefield.fields.VersatileImageField(null=True, upload_to=b'material/', blank=True),
        ),
        migrations.AddField(
            model_name='filmdirector',
            name='films',
            field=models.ManyToManyField(related_name='directors', to='festivaly.Film'),
        ),
    ]
