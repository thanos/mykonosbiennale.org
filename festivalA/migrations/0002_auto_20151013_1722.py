# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='participantrole_ptr',
        ),
        migrations.RemoveField(
            model_name='curator',
            name='participantrole_ptr',
        ),
        migrations.RemoveField(
            model_name='dancer',
            name='participantrole_ptr',
        ),
        migrations.RemoveField(
            model_name='director',
            name='participantrole_ptr',
        ),
        migrations.RemoveField(
            model_name='organiser',
            name='participantrole_ptr',
        ),
        migrations.RemoveField(
            model_name='participantrole',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='participantrole',
            name='polymorphic_ctype',
        ),
        migrations.DeleteModel(
            name='Art',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Curator',
        ),
        migrations.DeleteModel(
            name='Dancer',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Organiser',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.DeleteModel(
            name='ParticipantRole',
        ),
    ]
