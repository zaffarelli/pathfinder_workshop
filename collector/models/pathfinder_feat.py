from django.db import models
from django.contrib import admin


class PathfinderFeat(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Feat'
    name = models.CharField(max_length=64, default='', blank=True)
    is_fighter_feat = models.BooleanField(default=False)
    prerequisites = models.CharField(max_length=256, default='', blank=True)

    def __str__(self):
        return f'{self.name}'


class PathfinderFeatAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ['name', 'is_fighter_feat', 'prerequisites']
