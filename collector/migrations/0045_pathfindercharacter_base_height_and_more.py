# Generated by Django 4.0 on 2022-06-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0044_pathfinderlevel_is_giving_skill_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfindercharacter',
            name='base_height',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='pathfindercharacter',
            name='base_weight',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
