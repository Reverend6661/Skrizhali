# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=75)),
                ('content', tinymce.models.HTMLField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
