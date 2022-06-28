from django.db import models
from django.contrib import admin
from collector.models.pathfinder_gear import PathfinderGear, PathfinderGearAdmin


class PathfinderWeapon(PathfinderGear):
    class Meta:
        verbose_name = 'Pathfinder Weapon'

    DMG_small = models.CharField(default='1', max_length=24, blank=True)
    DMG_medium = models.CharField(default='1', max_length=24, blank=True)

    critical = models.CharField(default='x2', max_length=12, blank=True)

    attack_bonus = models.IntegerField(default=0, blank=True)
    DMG_bonus = models.IntegerField(default=0, blank=True)
    weapon_type = models.CharField(default='B', max_length=3, blank=True)
    weapon_class = models.CharField(default='Simple', max_length=32, blank=True)
    category = models.CharField(default='', max_length=256, blank=True)

    def __str__(self):
        if self.qualifier:
            return f'{self.qualifier} {self.name}'
        else:
            return f'{self.name}'

class PathfinderWeaponAdmin(PathfinderGearAdmin):
    ordering = ['weapon_class', 'weapon_type', 'name']
    list_display = ['name', 'qualifier', 'DMG_small', 'DMG_medium', 'critical', 'weapon_type', 'attack_bonus', 'DMG_bonus',
                    'gp_value', 'lbs_weight']
    list_filter = ['category', 'weapon_type', 'weapon_class']
