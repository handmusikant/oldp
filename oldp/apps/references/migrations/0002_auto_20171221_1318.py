# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-21 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casereferencemarker',
            name='text',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='lawreferencemarker',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
