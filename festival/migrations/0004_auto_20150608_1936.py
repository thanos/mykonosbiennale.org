# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0003_artist_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Art',
        ),
    ]
