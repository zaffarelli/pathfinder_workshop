# Generated by Django 4.0 on 2022-07-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0087_pathfinderweapon_reach_alter_pathfinderweapon_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfindercharacter',
            name='feats',
            field=models.ManyToManyField(to='collector.PathfinderFeat'),
        ),
    ]
