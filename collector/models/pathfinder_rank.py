from django.db import models
from django.contrib import admin
from collector.models.pathfinder_character import PathfinderCharacter
from collector.models.pathfinder_level import PathfinderLevel
from collector.models.pathfinder_skill import PathfinderSkill


class PathfinderRank(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Rank'

    character = models.ForeignKey(PathfinderCharacter, on_delete=models.CASCADE, blank=True, null=True)
    skill = models.ForeignKey(PathfinderSkill, on_delete=models.CASCADE, blank=True, null=True)
    rank = models.IntegerField(default=0, blank=True)
    max = models.IntegerField(default=1, blank=True)
    total = models.IntegerField(default=0, blank=True)
    racial_modifier = models.IntegerField(default=0, blank=True)
    other_modifier = models.IntegerField(default=0, blank=True)
    wildcard = models.CharField(default='', max_length=64, blank=True)

    class_skill_as = models.ForeignKey(PathfinderLevel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.character.name} {self.skill.name} {self.rank}'


class PathfinderRankInline(admin.TabularInline):
    model = PathfinderRank
    extras = 1
    ordering = ('skill', 'rank')


class PathfinderRankAdmin(admin.ModelAdmin):
    ordering = ["character", 'rank', 'skill', 'wildcard']
    list_display = ["character", 'skill', 'wildcard', 'rank']
