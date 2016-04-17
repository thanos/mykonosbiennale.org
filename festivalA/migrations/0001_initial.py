# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=128, blank=True)),
                ('slug', models.SlugField(max_length=128)),
                ('description', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('bio', models.TextField(default=b'', blank=True)),
                ('statement', models.TextField(default=b'', blank=True)),
                ('email', models.EmailField(default=b'', max_length=254, blank=True)),
                ('country', django_countries.fields.CountryField(default=b'', max_length=2, blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default=b'', max_length=128, blank=True)),
                ('homepage', models.URLField(default=b'', blank=True)),
                ('visible', models.BooleanField(default=True)),
                ('css', models.TextField(default=b'', blank=True)),
                ('javascript', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('participantrole_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivalA.ParticipantRole')),
                ('template', models.CharField(default=b'2015-artist.html', max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=('festivalA.participantrole',),
        ),
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('participantrole_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivalA.ParticipantRole')),
                ('field2', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('festivalA.participantrole',),
        ),
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('participantrole_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivalA.ParticipantRole')),
                ('field3', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('festivalA.participantrole',),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('participantrole_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivalA.ParticipantRole')),
                ('field3', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('festivalA.participantrole',),
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('participantrole_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivalA.ParticipantRole')),
                ('field2', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('festivalA.participantrole',),
        ),
        migrations.AddField(
            model_name='participantrole',
            name='participant',
            field=models.ForeignKey(to='festivalA.Participant'),
        ),
        migrations.AddField(
            model_name='participantrole',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_festivala.participantrole_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='art',
            name='artist',
            field=models.ForeignKey(to='festivalA.Artist'),
        ),
    ]
