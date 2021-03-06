# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-28 15:54
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magicbroomsite', '0040_auto_20170911_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationrequests',
            name='extra_service',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Clean Oven ($30)'), ('2', 'Clean Fridge ($30)'), ('3', 'Clean Interior Window ($25)'), ('4', 'Garage or Patio Sweep ($25)')], default=None, max_length=7, null=True),
        ),
    ]
