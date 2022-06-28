from django.db import models
from django.contrib import admin
from collector.utils.pathfinder_tools import ABILITIES_CHOICES


class PathfinderSkill(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Skill'
    name = models.CharField(max_length=64, default='', blank=True)
    is_trained_only = models.BooleanField(default=False)
    is_wildcard = models.BooleanField(default=False)
    ability = models.CharField(max_length=3, default='INT', choices=ABILITIES_CHOICES, blank=True)

    def __str__(self):
        return f'{self.name}'


class PathfinderSkillAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ['name', 'is_trained_only', 'is_wildcard', 'ability']
