# Generated by Django 4.0 on 2022-06-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0046_pathfinderweapon_dmg_medium_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderweapon',
            name='critical',
            field=models.CharField(blank=True, default='x2', max_length=12),
        ),
    ]
