from django.db import models
from django.contrib import admin


class PathfinderSpecialAbility(models.Model):
    class Meta:
        verbose_name_plural = 'Pathfinder Special Abilities'

    name = models.CharField(max_length=64, default='', blank=True)
    is_senses = models.BooleanField(default=False)
    is_skill_related = models.BooleanField(default=False)
    is_feat_related = models.BooleanField(default=False)
    is_offense_related = models.BooleanField(default=False)
    is_defense_related = models.BooleanField(default=False)
    is_abilities_bonus = models.BooleanField(default=False)
    is_spell_like_abilities = models.BooleanField(default=False)
    short_description = models.TextField(max_length=512, default='', blank=True)
    formula = models.TextField(default="", blank=True, max_length=256)

    def __str__(self):
        return f'{self.name}'


class PathfinderSpecialAbilityAdmin(admin.ModelAdmin):
    ordering = ['is_senses', 'is_skill_related', 'is_feat_related', 'is_abilities_bonus', 'is_offense_related',
                'is_defense_related', 'is_spell_like_abilities']
    list_display = ['name', 'formula', 'is_skill_related', 'is_feat_related', 'is_senses', 'is_abilities_bonus',
                    'is_offense_related', 'is_defense_related', 'is_spell_like_abilities', 'short_description']
