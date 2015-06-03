# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0006_auto_20150521_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='source',
            field=models.CharField(default=b'WITHOUTABOX', max_length=30, choices=[(b'WITHOUTABOX', b'Withoutabox'), (b'UNDECIDED', b'Filmfreeway'), (b'OUT', b'Other')]),
        ),
        migrations.AlterField(
            model_name='film',
            name='status',
            field=models.CharField(default=b'UNDECIDED', max_length=164, choices=[(b'SELECTED', b'Selected'), (b'UNDECIDED', b'Undecided'), (b'OUT', b'Out')]),
        ),
    ]
