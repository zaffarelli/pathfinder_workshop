# Generated by Django 4.0 on 2022-07-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0085_rename_base_height_pathfindercharacter_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderweapon',
            name='range',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
