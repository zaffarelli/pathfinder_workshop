# Generated by Django 4.0 on 2022-06-12 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0014_pathfinderarmor_arcane_spell_failure_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathfinderRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(blank=True, default=0)),
                ('total', models.IntegerField(blank=True, default=0)),
                ('racial_modifier', models.IntegerField(blank=True, default=0)),
                ('other_modifier', models.IntegerField(blank=True, default=0)),
                ('wildcard', models.CharField(blank=True, default='', max_length=64)),
                ('character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collector.pathfindercharacter')),
                ('skill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collector.pathfinderskill')),
            ],
            options={
                'verbose_name': 'Pathfinder Rank',
            },
        ),
    ]