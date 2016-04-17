# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0009_participant_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='tags',
            field=tagulous.models.fields.TagField(force_lowercase=True, initial=b'2013, 2013/artist, 2015', tree=True, to='festivalA.Tag', help_text='Enter a comma-separated tag string', _set_tag_meta=True),
        ),
    ]
