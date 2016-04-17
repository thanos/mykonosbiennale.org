# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0019_screening'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='original_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='film',
            name='film_type',
            field=models.CharField(default=b'Dramatic Nights', max_length=30, choices=[(b'Dramatic Nights', b'Dramatic Nights'), (b'Video Grafitti', b'Video Graffiti'), (b'Dance', b'Dance'), (b'Documentary', b'Documentary')]),
        ),
    ]
