# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170910_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollchoice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.PollQuestion'),
        ),
    ]