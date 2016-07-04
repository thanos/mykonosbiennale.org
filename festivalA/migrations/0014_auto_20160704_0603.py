# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0013_auto_20151028_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmSubmitter',
            fields=[
                ('participation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivalA.Participation')),
            ],
            options={
                'abstract': False,
            },
            bases=('festivalA.participation',),
        ),
        migrations.AlterField(
            model_name='art',
            name='tags',
            field=tagulous.models.fields.TagField(help_text='Enter a comma-separated tag string', autocomplete_view=b'festivalA_tag_autocomplete', to='festivalA.Tag', default=b'', _set_tag_meta=True, initial=b'2013, 2013/artist, 2015', tree=True, force_lowercase=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='year',
            field=models.IntegerField(default=2016),
        ),
        migrations.AlterField(
            model_name='participant',
            name='tags',
            field=tagulous.models.fields.TagField(help_text='Enter a comma-separated tag string', autocomplete_view=b'festivalA_tag_autocomplete', to='festivalA.Tag', default=b'', _set_tag_meta=True, initial=b'2013, 2013/artist, 2015', tree=True, force_lowercase=True),
        ),
    ]
