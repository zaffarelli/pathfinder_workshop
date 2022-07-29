# Generated by Django 4.0 on 2022-07-12 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0083_delete_pathfinderlegacy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_CHA',
            new_name='volatile_CHA',
        ),
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_CON',
            new_name='volatile_CON',
        ),
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_DEX',
            new_name='volatile_DEX',
        ),
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_INT',
            new_name='volatile_INT',
        ),
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_STR',
            new_name='volatile_STR',
        ),
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_WIS',
            new_name='volatile_WIS',
        ),
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_choice_racial_mod',
            new_name='volatile_choice_racial_mod',
        ),
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_hp',
            new_name='volatile_hp',
        ),
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='base_hwmod',
            new_name='volatile_hwmod',
        ),
        migrations.RenameField(
            model_name='pathfinderclass',
            old_name='base_age',
            new_name='volatile_age',
        ),
        migrations.RenameField(
            model_name='pathfinderclass',
            old_name='base_gold',
            new_name='volatile_gold',
        ),
    ]