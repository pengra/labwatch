# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 01:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engineer', models.BooleanField()),
                ('librarian', models.BooleanField()),
                ('techsavy', models.BooleanField()),
                ('beta_tester', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('auth_code', models.CharField(max_length=32, unique=True)),
                ('school_image', models.URLField()),
                ('primary_contact', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_contact_for', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Student First Name', max_length=255)),
                ('last_name', models.CharField(help_text='Student Last Name', max_length=255)),
                ('nick_name', models.CharField(blank=True, help_text="Should the student forget his ID, he can type his name or his/her 'nickname'.", max_length=255)),
                ('student_id', models.IntegerField(help_text='Student ID number', unique=True)),
                ('teacher', models.CharField(blank=True, help_text='Student teacher', max_length=255)),
                ('grade', models.CharField(blank=True, choices=[('09', 'Freshman'), ('10', 'Sophomore'), ('11', 'Junior'), ('12', 'Senior'), ('GD', 'Graduated')], max_length=2)),
                ('email', models.EmailField(blank=True, help_text='Student can submit email if they choose to', max_length=254)),
                ('signed_in', models.BooleanField(default=False, help_text='Status regarding student is signed in or not')),
                ('school', models.ForeignKey(help_text='School this student attends.', null=True, on_delete=django.db.models.deletion.CASCADE, to='baselabwatch.School')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires', models.DateTimeField()),
                ('billing_cycle', models.CharField(choices=[('one', 'One Time'), ('month', 'Monthly'), ('year', 'Yearly')], max_length=5)),
                ('max_student_ids', models.IntegerField()),
                ('max_kiosks', models.IntegerField()),
                ('max_logs', models.IntegerField()),
                ('student_rewards', models.BooleanField()),
                ('data_intel', models.BooleanField()),
                ('percentage_discount', models.FloatField()),
                ('numeric_discount', models.IntegerField()),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='baselabwatch.School')),
            ],
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('bug', 'Question'), ('question', 'Question')], max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('dealt_with', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='baselabwatch.School'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]