from django.db import models
from django.contrib import admin

GEAR_QUALITIES = (
    ('std', 'Standard'),
    ('mwk', 'Masterwork'),
)


class PathfinderGear(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Gear'

    name = models.CharField(max_length=64, default='', blank=True)
    quality = models.CharField(max_length=64, default='std', choices=GEAR_QUALITIES, blank=True)
    gp_value = models.PositiveIntegerField(default=0)
    pp_price = models.PositiveIntegerField(default=0)
    gp_price = models.PositiveIntegerField(default=0)
    sp_price = models.PositiveIntegerField(default=0)
    cp_price = models.PositiveIntegerField(default=0)
    lbs_weight = models.PositiveIntegerField(default=0)

    qualifier = models.CharField(max_length=64, default='', blank=True)

    is_weapon = models.BooleanField(default=False, blank=True)
    is_armor = models.BooleanField(default=False, blank=True)

    def fix(self):
        if self.gp_value == 0:
            self.gp_value = self.pp_price*10 + self.gp_price + self.sp_price/10 + self.cp_price/100

    def __str__(self):
        return f'{self.name}'

    @property
    def as_weapon(self):
        from collector.models.pathfinder_weapon import PathfinderWeapon
        if self.is_weapon:
            return PathfinderWeapon.objects.get(name=self.name)
        return None

    @property
    def as_armor(self):
        from collector.models.pathfinder_armor import PathfinderArmor
        if self.is_armor:
            return PathfinderArmor.objects.get(name=self.name)
        return None

class PathfinderGearAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ['name', 'gp_value', 'lbs_weight', 'is_weapon', 'is_armor']
