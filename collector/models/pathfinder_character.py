from django.db import models
from collector.models.character import Character
from collector.models.pathfinder_race import PathfinderRace
from django.contrib import admin


class PathfinderCharacter(Character):
    class Meta:
        verbose_name = 'Character'

    STR = models.IntegerField(default=0, blank=True, null=True)
    DEX = models.IntegerField(default=0, blank=True, null=True)
    CON = models.IntegerField(default=0, blank=True, null=True)
    INT = models.IntegerField(default=0, blank=True, null=True)
    WIS = models.IntegerField(default=0, blank=True, null=True)
    CHA = models.IntegerField(default=0, blank=True, null=True)

    base_STR = models.IntegerField(default=0, blank=True, null=True)
    base_DEX = models.IntegerField(default=0, blank=True, null=True)
    base_CON = models.IntegerField(default=0, blank=True, null=True)
    base_INT = models.IntegerField(default=0, blank=True, null=True)
    base_WIS = models.IntegerField(default=0, blank=True, null=True)
    base_CHA = models.IntegerField(default=0, blank=True, null=True)
    STR_racial_mod = models.IntegerField(default=0, blank=True)
    DEX_racial_mod = models.IntegerField(default=0, blank=True)
    CON_racial_mod = models.IntegerField(default=0, blank=True)
    INT_racial_mod = models.IntegerField(default=0, blank=True)
    WIS_racial_mod = models.IntegerField(default=0, blank=True)
    CHA_racial_mod = models.IntegerField(default=0, blank=True)
    race = models.ForeignKey(PathfinderRace, on_delete=models.SET_NULL, null=True, blank=True)

    def make_abilities(self):
        self.STR = self.base_STR + self.STR_racial_mod
        self.DEX = self.base_DEX + self.DEX_racial_mod
        self.CON = self.base_CON + self.CON_racial_mod
        self.INT = self.base_INT + self.INT_racial_mod
        self.WIS = self.base_WIS + self.WIS_racial_mod
        self.CHA = self.base_CHA + self.CHA_racial_mod

    def fix(self):
        super().fix()
        if self.need_fix:
            self.race.propagate(self)
            self.make_abilities()
            self.need_fix = False


def roll_standard_abilities(modeladmin, request, queryset):
    from collector.utils.pathfinder_tools import standard_method
    for c in queryset:
        c.base_STR = standard_method()
        c.base_DEX = standard_method()
        c.base_CON = standard_method()
        c.base_INT = standard_method()
        c.base_WIS = standard_method()
        c.base_CHA = standard_method()
        c.need_fix = True
        c.save()
    short_description = 'Roll Abilities (Standard)'


def roll_classic_abilities(modeladmin, request, queryset):
    from collector.utils.pathfinder_tools import classic_method
    for c in queryset:
        c.base_STR = classic_method()
        c.base_DEX = classic_method()
        c.base_CON = classic_method()
        c.base_INT = classic_method()
        c.base_WIS = classic_method()
        c.base_CHA = classic_method()
        c.need_fix = True
        c.save()
    short_description = 'Roll Abilities (Classic)'


class PathfinderCharacterAdmin(admin.ModelAdmin):
    from collector.models.pathfinder_class_level import PathfinderClassLevelInline
    list_display = ['name', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA', 'base_STR', 'base_DEX', 'base_CON', 'base_INT',
                    'base_WIS', 'base_CHA']
    actions = [roll_standard_abilities, roll_classic_abilities]
    inlines = [PathfinderClassLevelInline]
