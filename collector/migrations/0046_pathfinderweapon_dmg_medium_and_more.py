# Generated by Django 4.0 on 2022-06-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0045_pathfindercharacter_base_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderweapon',
            name='DMG_medium',
            field=models.CharField(blank=True, default='1', max_length=24),
        ),
        migrations.AddField(
            model_name='pathfinderweapon',
            name='DMG_small',
            field=models.CharField(blank=True, default='1', max_length=24),
        ),
        migrations.AddField(
            model_name='pathfinderweapon',
            name='category',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
