from django.db import models
from django.contrib import admin
from collector.models.pathfinder_special_ability import PathfinderSpecialAbility


class PathfinderRace(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Race'

    name = models.CharField(max_length=512, default='', blank=True)
    variant = models.CharField(max_length=512, default='', blank=True)
    STR_racial_mod = models.IntegerField(default=0, blank=True, verbose_name='STR')
    DEX_racial_mod = models.IntegerField(default=0, blank=True, verbose_name='DEX')
    CON_racial_mod = models.IntegerField(default=0, blank=True, verbose_name='CON')
    INT_racial_mod = models.IntegerField(default=0, blank=True, verbose_name='INT')
    WIS_racial_mod = models.IntegerField(default=0, blank=True, verbose_name='WIS')
    CHA_racial_mod = models.IntegerField(default=0, blank=True, verbose_name='CHA')

    CHOICE_racial_mod = models.IntegerField(default=0, blank=True)
    bonus_racial_feat = models.IntegerField(default=0, blank=True)
    bonus_racial_skill = models.IntegerField(default=0, blank=True)

    size = models.CharField(default='Medium', max_length=30, blank=True)
    speed = models.IntegerField(default=30, blank=True)
    category = models.CharField(default='Humanoid', max_length=30, blank=True)
    languages = models.CharField(default='', max_length=128, blank=True)

    number_of_favorite_classes = models.IntegerField(default=1, blank=True)

    starting_age_formula = models.CharField(default='', max_length=10, blank=True)

    special_abilities = models.ManyToManyField(PathfinderSpecialAbility)

    @property
    def abilities(self):
        # from collector.models.pathfinder_special_ability import PathfinderSpecialAbility
        list = self.special_abilities.all().values_list('name', flat=True)
        return ", ".join(list)+"."

    def __str__(self):
        return f'{self.category} ({self.name})'

    # def propagate(self, character):
    #     from collector.models.pathfinder_character import PathfinderCharacter
    #     from collector.utils.pathfinder_tools import choose_ability
    #     if isinstance(character, PathfinderCharacter):
    #         character.STR_racial_mod = self.STR_racial_mod
    #         character.DEX_racial_mod = self.DEX_racial_mod
    #         character.CON_racial_mod = self.CON_racial_mod
    #         character.INT_racial_mod = self.INT_racial_mod
    #         character.WIS_racial_mod = self.WIS_racial_mod
    #         character.CHA_racial_mod = self.CHA_racial_mod
    #         s = choose_ability()
    #         v = getattr(character, f'{s}_racial_mod')
    #         setattr(character, f'{s}_racial_mod', v + self.CHOICE_racial_mod)

    def roll_starting_age(self):
        from collector.utils.pathfinder_tools import die
        params = self.starting_age_formula.split(";")
        base = int(params[0])
        for n in range(int(params[1])):
            base += die(int(params[2]))


class PathfinderRaceAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'abilities', 'STR_racial_mod', 'DEX_racial_mod', 'CON_racial_mod', 'INT_racial_mod', 'WIS_racial_mod',
                    'CHA_racial_mod']
