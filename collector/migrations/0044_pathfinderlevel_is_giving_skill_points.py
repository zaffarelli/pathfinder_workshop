# Generated by Django 4.0 on 2022-06-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0043_pathfindercharacter_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderlevel',
            name='is_giving_skill_points',
            field=models.BooleanField(default=False),
        ),
    ]
