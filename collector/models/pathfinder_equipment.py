from django.db import models
from django.contrib import admin
from collector.models.pathfinder_gear import PathfinderGear
from collector.models.pathfinder_character import PathfinderCharacter


class PathfinderEquipment(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Equipment'

    character = models.ForeignKey(PathfinderCharacter, on_delete=models.CASCADE, blank=True, null=True)
    gear = models.ForeignKey(PathfinderGear, on_delete=models.CASCADE, blank=True, null=True)
    equipped = models.BooleanField(default=False, blank=True)


    def __str__(self):
        return f'{self.character.name} {self.gear}'


class PathfinderEquipmentInline(admin.TabularInline):
    model = PathfinderEquipment
    extras = 1
    ordering = ('character', 'gear')


class PathfinderEquipmentAdmin(admin.ModelAdmin):
    ordering = ["character", 'gear']
    list_display = ["character", 'gear', 'equipped']
