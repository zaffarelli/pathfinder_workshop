from django.db import models
from django.contrib import admin


class PathfinderClassFeature(models.Model):
    class Meta:
        verbose_name_plural = 'Pathfinder Class Features'
    name = models.CharField(max_length=64, default='', blank=True)
    feature_type = models.CharField(default="No", max_length=2, choices=(("No", "Normal"), ("Ex", "Extraordinary"), ("Su", "Supernatural"), ("Sp", "Spell Like Ability")))
    short_description = models.TextField(max_length=512, default='', blank=True)
    formula = models.TextField(default="", blank=True, max_length=256)

    def __str__(self):
        return f'{self.name}'


class PathfinderClassFeatureAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'feature_type','formula', 'short_description']
