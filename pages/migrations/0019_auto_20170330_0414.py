# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_page_menubar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='menubar',
            new_name='in_menubar',
        ),
    ]
