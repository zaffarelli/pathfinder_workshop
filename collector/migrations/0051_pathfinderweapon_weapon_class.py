# Generated by Django 4.0 on 2022-06-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0050_alter_pathfinderweapon_weapon_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderweapon',
            name='weapon_class',
            field=models.CharField(blank=True, default='Simple', max_length=32),
        ),
    ]
