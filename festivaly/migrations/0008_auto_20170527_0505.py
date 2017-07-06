# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festivaly', '0007_auto_20170527_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='art_directors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='cinematographers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='co_producers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='coming',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='composers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='contact_email',
            field=models.EmailField(default=b'', max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=b'', max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='country',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='crew',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='directors_statement',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='editors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='entry_status',
            field=models.CharField(default=b'undecided', max_length=20, choices=[(b'selected', b'selected'), (b'undecided', b'undecided'), (b'no', b'no')]),
        ),
        migrations.AddField(
            model_name='film',
            name='exec_producers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='facebook',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='film_type',
            field=models.CharField(default=b'short', max_length=20, choices=[(b'dance', b'dance'), (b'documentary', b'documentary'), (b'short', b'short'), (b'art_video', b'art_video')]),
        ),
        migrations.AddField(
            model_name='film',
            name='first_time',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='genres',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='info',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='log_line',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='niches',
            field=models.CharField(default=b'', max_length=256, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='original_title',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='other_social_media',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='photos',
            field=models.OneToOneField(related_name='film_of_photos', null=True, blank=True, to='festivaly.Album'),
        ),
        migrations.AddField(
            model_name='film',
            name='posted_on_facebook',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='poster',
            field=versatileimagefield.fields.VersatileImageField(null=True, upload_to=b'posters/', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='producers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='product_designers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='production_notes',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='projection_copy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='projection_copy_url',
            field=models.URLField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='runtime',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='screenings',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='screenwriters',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='sound_editors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='stills',
            field=models.OneToOneField(related_name='film_of_stills', null=True, blank=True, to='festivaly.Album'),
        ),
        migrations.AddField(
            model_name='film',
            name='sub_by',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='film',
            name='subtitles',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='synopsis',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='synopsis_125',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='synopsis_250',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='trailer_embed',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='trailer_url',
            field=models.URLField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='trailer_video',
            field=models.FileField(max_length=256, null=True, upload_to=b'material/', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='twitter',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='url',
            field=models.URLField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='when',
            field=models.CharField(default=b'', max_length=64, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.CharField(default=2017, max_length=4),
            preserve_default=False,
        ),
    ]
