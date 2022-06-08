from django.db import models
from django.contrib import admin




class PathfinderClass(models.Model):
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
    name = models.CharField(max_length=512, default='', blank=True)
    STR_favorite = models.IntegerField(default=0, blank=True)
    DEX_favorite = models.IntegerField(default=0, blank=True)
    CON_favorite = models.IntegerField(default=0, blank=True)
    INT_favorite = models.IntegerField(default=0, blank=True)
    WIS_favorite = models.IntegerField(default=0, blank=True)
    CHA_favorite = models.IntegerField(default=0, blank=True)

    CHOICE_racial_mod = models.IntegerField(default=0, blank=True)
    bonus_feat = models.IntegerField(default=0, blank=True)
    bonus_skill = models.IntegerField(default=0, blank=True)

    is_npc_class = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PathfinderClassAdmin(admin.ModelAdmin):
    list_display = ['name']
