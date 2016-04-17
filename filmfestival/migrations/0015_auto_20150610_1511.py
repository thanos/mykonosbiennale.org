# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0014_auto_20150610_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('slug', models.SlugField(max_length=200)),
                ('runtime', models.IntegerField(default=0)),
                ('time', models.TimeField(default=b'21:00')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pause', models.IntegerField(default=3)),
                ('slug', models.SlugField(max_length=200)),
                ('time', models.TimeField()),
                ('day', models.ForeignKey(to='filmfestival.Day')),
                ('film', models.ForeignKey(to='filmfestival.Film')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
        migrations.AddField(
            model_name='day',
            name='program',
            field=models.ForeignKey(to='filmfestival.Program'),
        ),
    ]
