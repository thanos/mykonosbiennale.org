# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivaly', '0003_participant_headshot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='albumn',
            new_name='album',
        ),
    ]
