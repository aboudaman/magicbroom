# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 13:23
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magicbroomsite', '0031_auto_20170909_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationrequests',
            name='extra_service',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Clean Oven'), ('2', 'Clean Fridge'), ('3', 'Clean Interior Window'), ('4', 'Garage or Patio Sweep')], default=None, max_length=7),
        ),
    ]
