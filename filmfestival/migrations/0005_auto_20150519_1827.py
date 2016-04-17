# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0004_auto_20150504_0328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['ref']},
        ),
        migrations.AlterField(
            model_name='documentation',
            name='title',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='film_type',
            field=models.CharField(default=b'Dramatic Nights', max_length=30, choices=[(b'Dramatic Nights', b'Dramatic Nights'), (b'Video Grafitti', b'Video Grafitti'), (b'Dance', b'Dance'), (b'Documentary', b'Documentary')]),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
    ]
