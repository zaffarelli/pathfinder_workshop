from django.db import models
from django.contrib import admin
from collector.models.pathfinder_class import PathfinderClass
from collector.models.pathfinder_class_feature import PathfinderClassFeature


class PathfinderClassAdvancement(models.Model):
    class Meta:
        verbose_name_plural = 'Pathfinder Class Advancement'

    pathfinder_class = models.ForeignKey(PathfinderClass, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0, blank=True)
    class_features = models.ManyToManyField(PathfinderClassFeature, blank=True)
    spd_0 = models.CharField(default='-', max_length=4, blank=True)
    spd_1 = models.CharField(default='-', max_length=4, blank=True)
    spd_2 = models.CharField(default='-', max_length=4, blank=True)
    spd_3 = models.CharField(default='-', max_length=4, blank=True)
    spd_4 = models.CharField(default='-', max_length=4, blank=True)
    spd_5 = models.CharField(default='-', max_length=4, blank=True)
    spd_6 = models.CharField(default='-', max_length=4, blank=True)
    spd_7 = models.CharField(default='-', max_length=4, blank=True)
    spd_8 = models.CharField(default='-', max_length=4, blank=True)
    spd_9 = models.CharField(default='-', max_length=4, blank=True)

    def __str__(self):
        return f'{self.pathfinder_class} level {self.level}'

    @property
    def label(self):
        return f'{self.pathfinder_class} level {self.level}'

    @property
    def features_list(self):
        list = []
        for feature in self.class_features.all():
            list.append(feature.name)
        return ', '.join(list)


class PathfinderClassAdvancementInline(admin.TabularInline):
    model = PathfinderClassAdvancement
    extras = 1
    ordering = ['level']


class PathfinderClassAdvancementAdmin(admin.ModelAdmin):
    ordering = ['pathfinder_class', 'level']
    list_display = ['label', 'level', 'spd_0', 'spd_1', 'spd_2', 'spd_3', 'spd_4', 'spd_5', 'spd_6', 'spd_7',
                    'spd_8', 'spd_9', 'features_list']
    list_filter = ['pathfinder_class', 'level']