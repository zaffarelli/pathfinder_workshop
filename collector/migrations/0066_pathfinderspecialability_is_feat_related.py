# Generated by Django 4.0 on 2022-07-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0065_pathfinderspecialability_is_spell_like_abilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathfinderspecialability',
            name='is_feat_related',
            field=models.BooleanField(default=False),
        ),
    ]