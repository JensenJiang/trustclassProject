# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 11:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databaseOperation', '0014_auto_20160907_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursereview',
            old_name='isNeutralRevivew',
            new_name='isNeutralReview',
        ),
    ]