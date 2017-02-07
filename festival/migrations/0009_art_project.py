# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0008_auto_20170206_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='project',
            field=models.ForeignKey(default=1, to='festival.Project'),
            preserve_default=False,
        ),
    ]
