# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_date']},
        ),
    ]
