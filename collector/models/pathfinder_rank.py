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
    # total = models.IntegerField(default=0, blank=True)
    ability_modifier = models.IntegerField(default=0, blank=True)
    racial_modifier = models.IntegerField(default=0, blank=True)
    other_modifier = models.IntegerField(default=0, blank=True)
    class_skill_bonus = models.PositiveIntegerField(default=0, blank=True)
    wildcard = models.CharField(default='', max_length=64, blank=True)
    details = models.CharField(default='', max_length=64, blank=True)

    class_skill_as = models.ForeignKey(PathfinderLevel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.character.name} {self.skill.name} {self.rank}'

    def fix_racial_modifier(self):
        pass

    def fix_class_modifier(self):
        pass

    def fix(self):
        self.fix_racial_modifier()
        self.fix_class_modifier()
        self.details = ""# f"[Rk:{self.rank}+Ab:{self.ability_modifier}+Ra:{self.racial_modifier}+CS:{self.class_skill_bonus}+Oth:{self.other_modifier}]"

    @property
    def total_score(self):
        x = self.rank
        x += self.ability_modifier
        x += self.racial_modifier
        x += self.other_modifier
        if self.rank > 0:
            x += self.class_skill_bonus
        return x

    @property
    def if_wildcard(self):
        str = ""
        if self.wildcard:
            str = f' ({self.wildcard})'
        return str



class PathfinderRankInline(admin.TabularInline):
    model = PathfinderRank
    extras = 1
    ordering = ['-rank', 'skill']


class PathfinderRankAdmin(admin.ModelAdmin):
    ordering = ["character", 'rank', 'skill', 'wildcard']
    list_display = ["character", 'skill', 'wildcard', 'rank', 'total_score']
