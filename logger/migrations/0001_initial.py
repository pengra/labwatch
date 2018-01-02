# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-02 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baselabwatch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(unique=True)),
                ('source', models.URLField(blank=True)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baselabwatch.School')),
            ],
        ),
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('auth_code', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PollQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_in_mode', models.CharField(choices=[('CARD', 'Card Scan'), ('NAME', 'Name input'), ('EMAL', 'Email'), ('NICK', 'Nickname input'), ('ADMI', 'Admin input')], max_length=4)),
                ('sign_out_mode', models.CharField(blank=True, choices=[('CARD', 'Card Scan'), ('NAME', 'Name input'), ('EMAL', 'Email'), ('NICK', 'Nickname input'), ('ADMI', 'Admin input')], max_length=4)),
                ('sign_in_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('sign_out_timestamp', models.DateTimeField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baselabwatch.Student')),
            ],
        ),
        migrations.AddField(
            model_name='pollchoice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logger.PollQuestion'),
        ),
        migrations.AddField(
            model_name='kiosk',
            name='poll',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logger.PollQuestion'),
        ),
        migrations.AddField(
            model_name='kiosk',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baselabwatch.School'),
        ),
    ]
