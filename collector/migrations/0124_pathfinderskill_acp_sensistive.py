# Generated by Django 4.0 on 2022-08-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0123_remove_pathfinderrace_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderskill',
            name='acp_sensistive',
            field=models.BooleanField(default=False),
        ),
    ]
