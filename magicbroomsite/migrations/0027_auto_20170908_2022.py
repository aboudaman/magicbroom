# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicbroomsite', '0026_auto_20170908_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationrequests',
            name='square_feet',
        ),
        migrations.AddField(
            model_name='quotationrequests',
            name='square_feet',
            field=models.CharField(default=None, max_length=155),
        ),
    ]
