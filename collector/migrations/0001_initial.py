# Generated by Django 4.0 on 2022-06-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PathfinderCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('rid', models.CharField(max_length=512)),
                ('need_fix', models.BooleanField(default=False)),
                ('base_STR', models.IntegerField(blank=True, default=0, null=True)),
                ('base_DEX', models.IntegerField(blank=True, default=0, null=True)),
                ('base_CON', models.IntegerField(blank=True, default=0, null=True)),
                ('base_INT', models.IntegerField(blank=True, default=0, null=True)),
                ('base_WIS', models.IntegerField(blank=True, default=0, null=True)),
                ('base_CHA', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
