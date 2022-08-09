from django.contrib import admin
from collector.models.pathfinder_level import PathfinderLevel


class PathfinderLevelInline(admin.TabularInline):
    model = PathfinderLevel
    extras = 1
    ordering = ('character_class', 'level')
