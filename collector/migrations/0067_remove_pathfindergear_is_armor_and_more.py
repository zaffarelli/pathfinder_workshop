# Generated by Django 4.0 on 2022-07-10 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0066_pathfinderspecialability_is_feat_related'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pathfindergear',
            name='is_armor',
        ),
        migrations.RemoveField(
            model_name='pathfindergear',
            name='is_weapon',
        ),
    ]
