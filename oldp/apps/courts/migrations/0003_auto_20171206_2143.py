# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_auto_20171206_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='image',
            field=models.ImageField(null=True, upload_to='courts'),
        ),
    ]
