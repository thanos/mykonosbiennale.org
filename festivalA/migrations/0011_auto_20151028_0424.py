# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0010_art_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='tags',
            field=tagulous.models.fields.TagField(to='festivalA.Tag', autocomplete_view=b'festivalA_tag_autocomplete', help_text='Enter a comma-separated tag string', _set_tag_meta=True, initial=b'2013, 2013/artist, 2015', tree=True, force_lowercase=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='tags',
            field=tagulous.models.fields.TagField(to='festivalA.Tag', autocomplete_view=b'festivalA_tag_autocomplete', help_text='Enter a comma-separated tag string', _set_tag_meta=True, initial=b'2013, 2013/artist, 2015', tree=True, force_lowercase=True),
        ),
    ]
