# Generated by Django 4.0 on 2022-06-09 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0009_pathfindergear_pathfinderweapon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfindergear',
            name='cp_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pathfindergear',
            name='gp_value',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pathfindergear',
            name='pp_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pathfindergear',
            name='sp_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
