# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicbroomsite', '0011_quotationrequests_home_info_boost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationrequests',
            name='home_info_boost',
            field=models.CharField(choices=[('1 bed', '1 bed'), ('2 bed', '2 bed'), ('3 bed', '3 bed')], default=None, max_length=155, null=True),
        ),
    ]
