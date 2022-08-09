from django.contrib import admin
from collector.models.pathfinder_character import PathfinderCharacter


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


def refix(modeladmin, request, queryset):
    from collector.utils.pathfinder_tools import classic_method
    for c in queryset:
        c.need_fix = True
        c.save()
    short_description = 'Refix'


class PathfinderCharacterAdmin(admin.ModelAdmin):
    from collector.models.pathfinder_level_inline import PathfinderLevelInline
    from collector.models.pathfinder_rank import PathfinderRankInline
    from collector.models.pathfinder_equipment import PathfinderEquipmentInline
    from collector.models.pathfinder_character_feat import PathfinderCharacterFeatInline
    ordering = ['-player', '-tcl']
    list_display = ['name', 'player', 'tcl', 'hp', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA', 'dm_notes']
    actions = [roll_standard_abilities, roll_classic_abilities, refix]
    inlines = [PathfinderLevelInline, PathfinderRankInline, PathfinderEquipmentInline,
               PathfinderCharacterFeatInline]
