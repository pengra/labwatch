# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-09 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='nick_name',
            field=models.CharField(blank=True, help_text="Should the student forget his ID, he can type his name or his/her 'nickname'.", max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, help_text='Student can submit email if they choose to', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(help_text='Student First Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(help_text='Student Last Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='signed_in',
            field=models.BooleanField(default=False, help_text='Status regarding student is signed in or not'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(help_text='Student ID number', unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.CharField(blank=True, help_text='Student teacher', max_length=255),
        ),
    ]