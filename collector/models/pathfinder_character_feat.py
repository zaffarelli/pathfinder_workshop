from django.db import models
from django.contrib import admin
from collector.models.pathfinder_character import PathfinderCharacter
from collector.models.pathfinder_feat import PathfinderFeat


class PathfinderCharacterFeat(models.Model):
    class Meta:
        verbose_name_plural = 'Pathfinder Character Feats'

    character = models.ForeignKey(PathfinderCharacter, on_delete=models.CASCADE, blank=True)
    feat = models.ForeignKey(PathfinderFeat, on_delete=models.CASCADE, blank=True)
    choice = models.TextField(default="", blank=True, max_length=256)

    def __str__(self):
        return f'{self.character.name} {self.feat.name}'


class PathfinderCharacterFeatInline(admin.TabularInline):
    model = PathfinderCharacterFeat
    extras = 1
    ordering = ['character', 'feat']


class PathfinderCharacterFeatAdmin(admin.ModelAdmin):
    ordering = ['character', 'feat']
    list_display = ['character', 'feat', 'choice']
