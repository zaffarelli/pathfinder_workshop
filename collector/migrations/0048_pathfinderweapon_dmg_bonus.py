# Generated by Django 4.0 on 2022-06-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0047_pathfinderweapon_critical'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderweapon',
            name='DMG_bonus',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
