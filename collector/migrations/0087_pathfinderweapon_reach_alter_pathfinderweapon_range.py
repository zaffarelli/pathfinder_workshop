# Generated by Django 4.0 on 2022-07-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0086_pathfinderweapon_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderweapon',
            name='reach',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='pathfinderweapon',
            name='range',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
