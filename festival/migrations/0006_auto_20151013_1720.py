# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0005_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='event',
            field=models.CharField(default=b'TREASURE HUNT', max_length=64, choices=[(b'ARCHEOLOGICAL MUSEUM', b'ARCHEOLOGICAL MUSEUM'), (b'TREASURE HUNT', b'TREASURE HUNT'), (b'KITE FESTIVAL', b'KITE FESTIVAL'), (b'PROJECT X', b'PROJECT X'), (b'INTERGRATIONS', b'INTERGRATIONS'), (b'PDF-JPEG', b'PDF-JPEG'), (b'OTHER', b'OTHER')]),
        ),
    ]
