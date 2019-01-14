# Generated by Django 2.1.2 on 2019-01-07 09:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0016_auto_20181211_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='source_file',
            field=models.FileField(blank=True, help_text='Original source file (only PDF allowed)', null=True, upload_to='cases/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]