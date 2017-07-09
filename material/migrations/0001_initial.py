# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import tagulous.models.fields
import tagulous.models.models
from django.db import models, migrations


class Migration(migrations.Migration):

    # dependencies = [
    #     ('photologue', '0011_auto_20170327_0213'),
    # ]

    operations = [
        migrations.CreateModel(
            name='_Tagulous_Album_tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gallery', models.OneToOneField(related_name='extended', to='photologue.Gallery')),
                ('tags', tagulous.models.fields.TagField(default=b'', help_text='Enter a comma-separated tag string', _set_tag_meta=True, to='material._Tagulous_Album_tags')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='_tagulous_album_tags',
            unique_together=set([('slug',)]),
        ),
    ]
