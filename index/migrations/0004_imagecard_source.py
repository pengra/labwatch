# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_imagecard'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecard',
            name='source',
            field=models.URLField(blank=True, unique=True),
        ),
    ]