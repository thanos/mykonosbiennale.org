# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0029_auto_20150727_0539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('award', models.ForeignKey(to='filmfestival.Award')),
                ('film', models.ForeignKey(to='filmfestival.Film')),
            ],
        ),
    ]
