# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseOperation', '0018_course_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Icon',
            field=models.CharField(default='settings', max_length=255),
        ),
    ]