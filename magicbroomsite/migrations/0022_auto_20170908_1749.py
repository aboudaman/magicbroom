# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicbroomsite', '0021_auto_20170906_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationrequests',
            name='home_info_boost',
            field=models.CharField(default=None, max_length=155),
        ),
        migrations.AlterField(
            model_name='quotationrequests',
            name='zip_code',
            field=models.CharField(max_length=5),
        ),
    ]
