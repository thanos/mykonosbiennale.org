# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0002_auto_20150608_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='event',
            field=models.CharField(default=b'TEASURE HUNT', max_length=64, choices=[(b'TEASURE HUNT', b'TEASURE HUNT'), (b'KITE FESTIVAL', b'KITE FESTIVAL'), (b'OTHER', b'OTHER')]),
        ),
    ]
