# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Album'},
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to='albums/static'),
        ),
    ]
