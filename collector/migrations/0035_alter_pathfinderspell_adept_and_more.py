# Generated by Django 4.0 on 2022-06-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0034_pathfindercharacter_init_pathfindercharacter_senses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathfinderspell',
            name='adept',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='alchemist',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='antipaladin',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='bard',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='cleric',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='druid',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='inquisitor',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='magus',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='oracle',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='paladin',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='ranger',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='sor',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='summoner',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='witch',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='wiz',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
    ]