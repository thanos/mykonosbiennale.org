# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0012_auto_20170517_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='project_x',
            field=models.ForeignKey(blank=True, to='festival.ProjectSeason', null=True),
        ),
    ]
