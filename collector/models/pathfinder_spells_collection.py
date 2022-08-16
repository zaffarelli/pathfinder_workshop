from django.db import models
from django.contrib import admin


# from collector.models.pathfinder_level import PathfinderLevel


class PathfinderSpellsCollection(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Spells Collection'

    name = models.CharField(default="", max_length=128)
    is_finished = models.BooleanField(default=False)

    @property
    def spells(self):
        list = []
        for s in self.pathfinderspell_set.all():
            list.append(f"{s.name} {s.SLA_Level}")
        return ", ".join(list)

    @property
    def spells_list(self):
        list = []
        for s in self.pathfinderspell_set.all().order_by("SLA_Level","name"):
            list.append({"name": s.name, "level": s.SLA_Level, 'short_description': s.short_description, "domain": s.domain})
        return list

    def __str__(self):
        return f'Spells for {self.name}'


class PathfinderSpellsCollectionAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', "spells"]
