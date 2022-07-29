from django.db import models
from django.contrib import admin
from collector.utils.pathfinder_tools import BABRates, SaveRates, ABILITIES_CHOICES
from collector.models.pathfinder_class_feature import PathfinderClassFeature


class PathfinderClass(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Class'
        verbose_name_plural = 'Pathfinder Classes'

    name = models.CharField(max_length=512, default='', blank=True)
    STR_favorite = models.IntegerField(default=0, blank=True)
    DEX_favorite = models.IntegerField(default=0, blank=True)
    CON_favorite = models.IntegerField(default=0, blank=True)
    INT_favorite = models.IntegerField(default=0, blank=True)
    WIS_favorite = models.IntegerField(default=0, blank=True)
    CHA_favorite = models.IntegerField(default=0, blank=True)

    volatile_age = models.IntegerField(default=0, blank=True)
    volatile_gold = models.PositiveIntegerField(default=0, blank=True)

    main_ability = models.CharField(max_length=3, default='---', choices=ABILITIES_CHOICES, blank=True)

    BAB_rate = models.CharField(max_length=4, choices=BABRates, default='MBAB')
    fort_rate = models.CharField(max_length=5, choices=SaveRates, default='BSAVE')
    ref_rate = models.CharField(max_length=5, choices=SaveRates, default='BSAVE')
    will_rate = models.CharField(max_length=5, choices=SaveRates, default='BSAVE')

    languages = models.CharField(default='', max_length=128, blank=True)

    bonus_feat = models.IntegerField(default=0, blank=True)
    bonus_skill = models.IntegerField(default=0, blank=True)

    is_npc_class = models.BooleanField(default=False)
    is_spellcasting_class = models.BooleanField(default=False)

    skill_ranks_per_level = models.IntegerField(default=2, blank=True)
    hit_die = models.IntegerField(default=4, blank=True)

    class_skills = models.TextField(max_length=2048, default="", blank=True)

    def __str__(self):
        return self.name

    def current_caster_level(self, level):
        from collector.models.pathfinder_advancement import PathfinderClassAdvancement
        caster_level = self.pathfinderclassadvancement_set.filter(level=level)
        max_spell_level = 1
        class_column = self.name
        if len(caster_level) == 1:
            return caster_level.first(), max_spell_level, class_column
        else:
            return None, None, None


class PathfinderClassAdmin(admin.ModelAdmin):
    from collector.models.pathfinder_advancement import PathfinderClassAdvancementInline
    ordering = ['is_npc_class', 'name']
    list_display = ['name', 'main_ability', 'is_npc_class', 'is_spellcasting_class', 'BAB_rate', 'fort_rate', 'ref_rate',
                    'will_rate', 'skill_ranks_per_level', 'hit_die', "class_skills"]
    inlines = [PathfinderClassAdvancementInline]
