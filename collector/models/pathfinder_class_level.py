from django.db import models
from django.contrib import admin
from collector.models.pathfinder_class import PathfinderClass
from collector.models.pathfinder_character import PathfinderCharacter


class PathfinderClassLevel(models.Model):
    class Meta:
        verbose_name = 'Class-Level'
        verbose_name_plural = 'Class-Levels'

    character = models.ForeignKey(PathfinderCharacter, on_delete=models.CASCADE)
    character_class = models.ForeignKey(PathfinderClass, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f'({self.character.name}) {self.character_class} level {self.level} '


class PathfinderClassLevelInline(admin.TabularInline):
    model = PathfinderClassLevel
    extras = 1
    ordering = ('character_class', 'level')


class PathfinderClassLevelAdmin(admin.ModelAdmin):
    list_display = ['character', 'character_class', 'level', 'is_favorite']
