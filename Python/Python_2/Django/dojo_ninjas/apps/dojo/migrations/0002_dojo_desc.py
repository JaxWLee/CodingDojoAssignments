# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-18 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='We are helping future developers get the jobs they want'),
        ),
    ]
