# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0026_auto_20150620_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='trailer',
            new_name='trailer_url',
        ),
        migrations.AddField(
            model_name='film',
            name='trailer_embed',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
