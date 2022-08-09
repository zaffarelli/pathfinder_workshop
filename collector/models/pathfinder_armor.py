from django.db import models
from django.contrib import admin
from collector.models.pathfinder_gear import PathfinderGear, PathfinderGearAdmin


class PathfinderArmor(PathfinderGear):
    class Meta:
        verbose_name = 'Pathfinder Armor'

    AC_bonus = models.IntegerField(default=0, blank=True)
    max_dex_bonus = models.IntegerField(default=0, blank=True)
    armor_check_penalty = models.IntegerField(default=0, blank=True)
    arcane_spell_failure = models.IntegerField(default=0, blank=True)
    category = models.CharField(default='', max_length=256, blank=True)
    is_shield = models.BooleanField(default=False, blank=True)
    speed_30 = models.IntegerField(default=30, blank=True)
    speed_20 = models.IntegerField(default=20, blank=True)


class PathfinderArmorAdmin(PathfinderGearAdmin):
    ordering = ['category', 'AC_bonus', 'name']
    list_display = ['name', 'category', 'gp_value', 'AC_bonus', 'lbs_weight', 'armor_check_penalty', 'speed_30', 'speed_20']
    list_filter = ['category', 'is_shield']
