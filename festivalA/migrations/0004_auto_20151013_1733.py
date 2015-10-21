# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0003_auto_20151013_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='artist',
            new_name='directed_by',
        ),
    ]
