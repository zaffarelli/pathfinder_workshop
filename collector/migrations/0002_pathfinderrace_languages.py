# Generated by Django 4.0 on 2022-06-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderrace',
            name='languages',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
