from django.db import models
from django.contrib import admin
from collector.models.pathfinder_class import PathfinderClass
from collector.models.pathfinder_character import PathfinderCharacter
from collector.models.pathfinder_spells_collection import PathfinderSpellsCollection
from collector.utils.pathfinder_tools import get_modifier, ABILITIES_CHOICES
import math


class PathfinderLevel(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Level'

    character = models.ForeignKey(PathfinderCharacter, on_delete=models.CASCADE)
    character_class = models.ForeignKey(PathfinderClass, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)
    is_favorite = models.BooleanField(default=False)
    # is_giving_skill_points = models.BooleanField(default=False)
    favored_skill_points = models.PositiveIntegerField(default=0)
    favored_hit_points = models.PositiveIntegerField(default=0)
    deity = models.CharField(default='', max_length=128, blank=True)
    domains = models.CharField(default='', max_length=128, blank=True)
    spells_collection = models.ForeignKey(PathfinderSpellsCollection, on_delete=models.CASCADE, null=True, blank=True)
    custom_fields = models.CharField(default='', max_length=256, blank=True)

    spellcasting_ability = models.CharField(max_length=3, default='---', choices=ABILITIES_CHOICES, blank=True)

    def __str__(self):
        return f'({self.character.name}) {self.character_class} level {self.level} '

    @property
    def class_level(self):
        return f'{self.character_class} {self.level} '

    @property
    def base_attack_bonus(self):
        # Todo: Handle supplementary attacks
        bab = 0
        if self.character_class.BAB_rate == 'FBAB':
            bab = self.level
        elif self.character_class.BAB_rate == 'MBAB':
            bab = (self.level - 1) % 4 + 3 * math.floor(self.level - 1 / 4)
        elif self.character_class.BAB_rate == 'SBAB':
            bab = math.floor(self.level / 2)
        return bab

    def fortitude_bonus(self):
        score = 0
        if self.character_class.fort_rate == 'GSAVE':
            score = math.ceil(self.level / 2) + 1
        elif self.character_class.fort_rate == 'BSAVE':
            score = math.floor(self.level / 3)
        return score

    def reflex_bonus(self):
        score = 0
        if self.character_class.ref_rate == 'GSAVE':
            score = math.ceil(self.level / 2) + 1
        elif self.character_class.ref_rate == 'BSAVE':
            score = math.floor(self.level / 3)
        return score

    def will_bonus(self):
        score = 0
        if self.character_class.will_rate == 'GSAVE':
            score = math.ceil(self.level / 2) + 1
        elif self.character_class.will_rate == 'BSAVE':
            score = math.floor(self.level / 3)
        return score

    @property
    def total_ranks(self):
        r = 0
        r += get_modifier(getattr(self.character, "INT"))
        r += self.character_class.skill_ranks_per_level
        return r * self.level + self.favored_skill_points

    @property
    def spells_list(self):
        if self.spells_collection:
            return self.spells_collection.spells_list
        else:
            return []

    def fix(self):
        if self.character_class.is_spellcasting_class:
            print(self.character.name, 'level fixed')
            if self.spells_collection is None:
                sc = PathfinderSpellsCollection()
                self.spells_collection = sc
                self.spells_collection.save()
                self.save()
            self.spells_collection.name = f'{self.character.name} as {self.class_level}'
            self.spells_collection.save()
        else:
            self.spells_collection = None

    @property
    def current_caster_level(self):
        if self.character_class.caster_level < 20:
            x = self.level + self.character_class.caster_level
            if x < 0:
                x = 0
            return x
        else:
            return 0

    def autofill_spells_collection(self):
        from collector.models.pathfinder_spell import PathfinderSpell
        print("AUTOFILL")
        if self.spells_collection:
            self.spells_collection.pathfinderspell_set.clear()
            adv = self.character_class.pathfinderclassadvancement_set.filter(level=self.level,
                                                                             pathfinder_class=self.character_class)
            max_spell_level = adv.first().max_spell_level
            if self.character_class.name.lower() == 'cleric':
                their_spell_list = PathfinderSpell.objects.filter(source="PFRPG Core",
                                                                  cleric__lte=max_spell_level).order_by('cleric',
                                                                                                        'name')
            elif self.character_class.name.lower() == 'druid':
                their_spell_list = PathfinderSpell.objects.filter(source="PFRPG Core",
                                                                  druid__lte=max_spell_level).order_by('druid', 'name')
            elif self.character_class.name.lower() == 'paladin':
                their_spell_list = PathfinderSpell.objects.filter(source="PFRPG Core",
                                                                  paladin__lte=max_spell_level).order_by('paladin',
                                                                                                         'name')
            elif self.character_class.name.lower() == 'ranger':
                their_spell_list = PathfinderSpell.objects.filter(source="PFRPG Core",
                                                                  ranger__lte=max_spell_level).order_by('ranger',
                                                                                                        'name')
            else:
                their_spell_list = []
            for s in their_spell_list:
                self.spells_collection.pathfinderspell_set.add(s)
                print(s.name)
            self.spells_collection.save()

    @property
    def active_features(self):
        list = []
        final_list = {}
        for adv in self.character_class.pathfinderclassadvancement_set.filter(level__lte=self.level):
            for feature in adv.class_features.all():
                list.append(feature.name)
        for key in list:
            if key in final_list:
                final_list[key] = final_list[key] + 1
            else:
                final_list[key] = 1

        return final_list

    @property
    def spd(self):
        from collector.utils.pathfinder_tools import TABLE_1_3
        list = []
        advs = self.character_class.pathfinderclassadvancement_set.filter(level=self.level)
        score = getattr(self.character,self.spellcasting_ability)
        print(score)
        row = TABLE_1_3[score]
        print(row)
        if len(advs) == 1:
            adv = advs.first()
            for x in range(0, 10):
                if x > 0:
                    v = row[str(x)]
                else:
                    v = 0
                list.append({"level": x, "spd": getattr(adv, "spd_" + str(x)), "ability_bonus": v})
        return list


class PathfinderLevelAdmin(admin.ModelAdmin):
    list_display = ['character', 'character_class', 'level', 'is_favorite', 'spellcasting_ability', 'current_caster_level', 'spells_collection',
                    'active_features', 'custom_fields']
