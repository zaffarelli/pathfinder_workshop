# Generated by Django 4.0 on 2022-08-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0128_remove_pathfinderlevel_caster_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderclass',
            name='uses_custom_spells_collection',
            field=models.BooleanField(default=False),
        ),
    ]