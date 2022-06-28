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



class PathfinderArmorAdmin(PathfinderGearAdmin):
    list_display = ['name','AC_bonus', 'max_dex_bonus', 'armor_check_penalty', 'arcane_spell_failure']
