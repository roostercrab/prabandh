# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name_plural': 'Faculties'},
        ),
        migrations.AlterModelOptions(
            name='sakha',
            options={'verbose_name_plural': 'Sakhayein'},
        ),
    ]
