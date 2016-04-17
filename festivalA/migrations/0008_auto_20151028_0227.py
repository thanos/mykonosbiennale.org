# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0007_auto_20151028_0204'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='_tagulous_participant_tags',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='_tagulous_participant_tags',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='tags',
        ),
        migrations.DeleteModel(
            name='_Tagulous_Participant_tags',
        ),
    ]
