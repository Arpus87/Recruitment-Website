# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 14:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypt', '0015_auto_20160708_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptrecdata',
            name='rollno',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid Roll number.', regex='^(\\d{2}|\\d{8})?([a-z]{2}|[A-Z]{2})\\d{2,3}([a-z]{1}|[A-Z]{1})?$')]),
        ),
    ]