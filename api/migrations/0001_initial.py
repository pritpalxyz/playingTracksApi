# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import api.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contentInEnglish', models.TextField(null=True, verbose_name='About in English', blank=True)),
                ('contentInSpanish', models.TextField(null=True, verbose_name='About in Spanish', blank=True)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='folder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('NameInEnglish', models.CharField(max_length=200, verbose_name='Book in English')),
                ('NameInSpanish', models.CharField(max_length=200, verbose_name='Book in Spanish')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='privacyPolicy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contentInEnglish', models.TextField(null=True, verbose_name='Privacy Policy in English', blank=True)),
                ('contentInSpanish', models.TextField(null=True, verbose_name='Privacy Policy in Spanish', blank=True)),
            ],
            options={
                'verbose_name': 'Privacy Policy',
                'verbose_name_plural': 'Privacy Policy',
            },
        ),
        migrations.CreateModel(
            name='tracks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('TrackNameInEnglish', models.CharField(max_length=200, verbose_name='Chapter in English')),
                ('TrackNameInSpanish', models.CharField(max_length=200, verbose_name='Chapter in Spanish')),
                ('TrackPath', models.FileField(upload_to=api.models.get_capture_upload_path, verbose_name='Upload Chapter')),
                ('FolderAssociated', models.ForeignKey(verbose_name='Select Book', to='api.folder')),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
            },
        ),
    ]
