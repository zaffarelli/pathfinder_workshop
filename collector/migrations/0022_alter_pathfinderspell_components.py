# Generated by Django 4.0 on 2022-06-15 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0021_alter_pathfinderspell_targets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathfinderspell',
            name='components',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]