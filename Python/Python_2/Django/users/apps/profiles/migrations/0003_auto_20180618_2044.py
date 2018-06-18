# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-18 20:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180618_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='has to be 8 letters', regex='^/w{8}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
    ]