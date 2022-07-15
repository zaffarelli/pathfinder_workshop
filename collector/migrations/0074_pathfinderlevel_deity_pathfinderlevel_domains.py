# Generated by Django 4.0 on 2022-07-12 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0073_pathfindercharacter_dm_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderlevel',
            name='deity',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='pathfinderlevel',
            name='domains',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
