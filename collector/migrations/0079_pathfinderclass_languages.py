# Generated by Django 4.0 on 2022-07-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0078_pathfinderrank_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderclass',
            name='languages',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
