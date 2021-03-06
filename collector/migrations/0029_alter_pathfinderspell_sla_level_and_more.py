# Generated by Django 4.0 on 2022-06-15 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0028_alter_pathfinderspell_sla_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathfinderspell',
            name='SLA_Level',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='area',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='bloodline',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='bloodrager',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='casting_time',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='costly_components',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='deity',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='descriptor',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='dismissible',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='domain',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='effect',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='haunt_statistics',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='hunter',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='investigator',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='linktext',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='material_costs',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='medium',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='mesmerist',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='name',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='occultist',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='patron',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='psychic',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='range',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='saving_throw',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='school',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='shaman',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='shapeable',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='skald',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='source',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='spiritualist',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='src_id',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='subschool',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='pathfinderspell',
            name='summoner_unchained',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
