# Generated by Django 4.0 on 2022-07-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0070_remove_pathfinderrank_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderspecialability',
            name='formula',
            field=models.TextField(blank=True, default='', max_length=256),
        ),
    ]
