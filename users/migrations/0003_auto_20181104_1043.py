# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-11-04 05:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160806_2306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='learner',
            options={'ordering': ['user__first_name', 'user__last_name']},
        ),
    ]