# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('release_year', models.CharField(max_length=4)),
                ('cover', models.ImageField(upload_to=b'')),
                ('link', models.URLField(max_length=100)),
                ('songs_list', models.TextField()),
            ],
        ),
    ]
