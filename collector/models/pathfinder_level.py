from django.db import models
from django.contrib import admin
from collector.models.pathfinder_class import PathfinderClass
from collector.models.pathfinder_character import PathfinderCharacter
import math


class PathfinderLevel(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Level'

    character = models.ForeignKey(PathfinderCharacter, on_delete=models.CASCADE)
    character_class = models.ForeignKey(PathfinderClass, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)
    is_favorite = models.BooleanField(default=False)
    # is_giving_skill_points = models.BooleanField(default=False)
    favored_skill_points = models.PositiveIntegerField(default=0)
    favored_hit_points = models.PositiveIntegerField(default=0)
    deity = models.CharField(default='', max_length=128, blank=True)
    domains = models.CharField(default='', max_length=128, blank=True)

    def __str__(self):
        return f'({self.character.name}) {self.character_class} level {self.level} '

    @property
    def class_level(self):
        return f'{self.character_class} {self.level} '

    @property
    def base_attack_bonus(self):
        # Todo: Handle supplementary attacks
        bab = 0
        if self.character_class.BAB_rate == 'FBAB':
            bab = self.level
        elif self.character_class.BAB_rate == 'MBAB':
            bab = (self.level - 1) % 4 + 3 * math.floor(self.level - 1 / 4)
        elif self.character_class.BAB_rate == 'SBAB':
            bab = math.floor(self.level / 2)
        return bab

    def fortitude_bonus(self):
        score = 0
        if self.character_class.fort_rate == 'GSAVE':
            score = math.ceil(self.level / 2) + 1
        elif self.character_class.fort_rate == 'BSAVE':
            score = math.floor(self.level / 3)
        return score

    def reflex_bonus(self):
        score = 0
        if self.character_class.ref_rate == 'GSAVE':
            score = math.ceil(self.level / 2) + 1
        elif self.character_class.ref_rate == 'BSAVE':
            score = math.floor(self.level / 3)
        return score

    def willpower_bonus(self):
        score = 0
        if self.character_class.will_rate == 'GSAVE':
            score = math.ceil(self.level / 2) + 1
        elif self.character_class.will_rate == 'BSAVE':
            score = math.floor(self.level / 3)
        return score


class PathfinderLevelInline(admin.TabularInline):
    model = PathfinderLevel
    extras = 1
    ordering = ('character_class', 'level')


class PathfinderLevelAdmin(admin.ModelAdmin):
    list_display = ['character', 'character_class', 'level', 'is_favorite']
