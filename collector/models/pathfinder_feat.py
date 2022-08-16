from django.db import models
from django.contrib import admin


class PathfinderFeat(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Feat'

    name = models.CharField(max_length=64, default='', blank=True)
    is_fighter_feat = models.BooleanField(default=False)
    is_skill_related = models.BooleanField(default=False)
    is_save_related = models.BooleanField(default=False)
    is_metamagic = models.BooleanField(default=False)
    is_item_creation = models.BooleanField(default=False)

    formula = models.CharField(default='', max_length=128, blank=True)
    target = models.CharField(default='', max_length=128, blank=True)
    prerequisites = models.CharField(max_length=256, default='', blank=True)
    short_description = models.TextField(max_length=256, default='', blank=True)

    def __str__(self):
        return f'{self.name}'


class PathfinderFeatAdmin(admin.ModelAdmin):
    ordering = ['is_save_related', 'is_metamagic', 'is_item_creation','is_fighter_feat', 'is_skill_related',"name"]
    list_display = ['name', 'is_fighter_feat', 'is_skill_related', 'is_save_related', 'is_metamagic', 'is_item_creation','formula', 'prerequisites', 'short_description']
    list_filter = ['is_fighter_feat', 'is_skill_related', 'is_save_related', 'is_metamagic', 'is_item_creation']
