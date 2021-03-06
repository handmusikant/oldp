# Generated by Django 2.1.2 on 2019-01-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0003_auto_20181223_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='value_float',
            field=models.FloatField(default=0, help_text='Content as number that represents the entity (for e.g. money)'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='pos_end',
            field=models.IntegerField(help_text='End position of entity in content', null=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='pos_start',
            field=models.IntegerField(help_text='Start position of entity in content', null=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='type',
            field=models.CharField(choices=[('MONEY', 'Monetary values with currency.'), ('EURO', 'Euro amounts.'), ('PERSON', 'Name of a person or family.'), ('LOCATION', 'Name of geographical or political locations.'), ('ORGANIZATION', 'Any organizational entity.'), ('PERCENT', 'Percentage amounts.')], default='MONEY', help_text='Entity type', max_length=12),
        ),
        migrations.AlterField(
            model_name='entity',
            name='value',
            field=models.TextField(help_text='Content that represents the entity'),
        ),
    ]
