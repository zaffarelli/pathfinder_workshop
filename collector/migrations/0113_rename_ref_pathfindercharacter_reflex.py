# Generated by Django 4.0 on 2022-08-04 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0112_rename_fort_pathfindercharacter_fortitude_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pathfindercharacter',
            old_name='ref',
            new_name='reflex',
        ),
    ]
