# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivaly', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['sort_by']},
        ),
        migrations.AlterModelOptions(
            name='festival',
            options={'ordering': ['-year']},
        ),
        migrations.AlterModelOptions(
            name='festivalproject',
            options={'ordering': ['sort_by']},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['sort_by']},
        ),
        migrations.AlterModelOptions(
            name='participant',
            options={'ordering': ['sort_by']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['sort_by']},
        ),
        migrations.RemoveField(
            model_name='participant',
            name='bio',
        ),
    ]
