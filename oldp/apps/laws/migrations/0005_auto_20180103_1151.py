# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-03 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0004_auto_20171222_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawbook',
            name='code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
