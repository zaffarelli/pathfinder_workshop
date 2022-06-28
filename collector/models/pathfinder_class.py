from django.db import models
from django.contrib import admin
from collector.utils.pathfinder_tools import BABRates, SaveRates


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

    base_age = models.IntegerField(default=0, blank=True)

    # base_attack_bonus = models.IntegerField(default=0, blank=True)
    # base_fort = models.IntegerField(default=0, blank=True)
    # base_ref = models.IntegerField(default=0, blank=True)
    # base_will = models.IntegerField(default=0, blank=True)

    base_gold = models.PositiveIntegerField(default=0, blank=True)

    BAB_rate = models.CharField(max_length=4, choices=BABRates, default='MBAB')
    fort_rate = models.CharField(max_length=5, choices=SaveRates, default='BSAVE')
    ref_rate = models.CharField(max_length=5, choices=SaveRates, default='BSAVE')
    will_rate = models.CharField(max_length=5, choices=SaveRates, default='BSAVE')

    bonus_feat = models.IntegerField(default=0, blank=True)
    bonus_skill = models.IntegerField(default=0, blank=True)

    is_npc_class = models.BooleanField(default=False)

    skill_ranks_per_level = models.IntegerField(default=2, blank=True)
    hit_die = models.IntegerField(default=4, blank=True)

    class_skills = models.TextField(max_length=2048, default="", blank=True)

    def __str__(self):
        return self.name


class PathfinderClassAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'is_npc_class', 'skill_ranks_per_level', 'hit_die', "class_skills"]
