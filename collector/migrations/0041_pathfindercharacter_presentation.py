# Generated by Django 4.0 on 2022-06-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0040_pathfinderclass_bab_rate_pathfinderclass_fort_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfindercharacter',
            name='presentation',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
    ]