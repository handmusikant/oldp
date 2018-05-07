# Generated by Django 2.0.4 on 2018-04-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20180425_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='sections',
        ),
        migrations.AddField(
            model_name='case',
            name='content',
            field=models.TextField(default='', help_text='Case full-text formatted in Legal Markdown'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='ecli',
            field=models.CharField(blank=True, help_text='European Case Law Identifier', max_length=255),
        ),
        migrations.AlterField(
            model_name='case',
            name='text',
            field=models.TextField(help_text='Plain full-text for searching', null=True),
        ),
    ]
