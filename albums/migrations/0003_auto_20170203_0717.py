# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 07:17
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_auto_20161230_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='songs_list',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
