from django.db import models
from collector.models.character import Character
from collector.models.pathfinder_race import PathfinderRace
from collector.utils.pathfinder_tools import as_modifier, ABILITIES_CHOICES
from django.contrib import admin


class PathfinderCharacter(Character):
    class Meta:
        verbose_name = 'Pathfinder Character'

    player = models.CharField(max_length=128, default='', blank=True)

    STR = models.IntegerField(default=0, blank=True, null=True)
    DEX = models.IntegerField(default=0, blank=True, null=True)
    CON = models.IntegerField(default=0, blank=True, null=True)
    INT = models.IntegerField(default=0, blank=True, null=True)
    WIS = models.IntegerField(default=0, blank=True, null=True)
    CHA = models.IntegerField(default=0, blank=True, null=True)

    base_STR = models.IntegerField(default=0, blank=True, null=True)
    base_DEX = models.IntegerField(default=0, blank=True, null=True)
    base_CON = models.IntegerField(default=0, blank=True, null=True)
    base_INT = models.IntegerField(default=0, blank=True, null=True)
    base_WIS = models.IntegerField(default=0, blank=True, null=True)
    base_CHA = models.IntegerField(default=0, blank=True, null=True)
    # STR_racial_mod = models.IntegerField(default=0, blank=True)
    # DEX_racial_mod = models.IntegerField(default=0, blank=True)
    # CON_racial_mod = models.IntegerField(default=0, blank=True)
    # INT_racial_mod = models.IntegerField(default=0, blank=True)
    # WIS_racial_mod = models.IntegerField(default=0, blank=True)
    # CHA_racial_mod = models.IntegerField(default=0, blank=True)

    base_hp = models.IntegerField(default=0, blank=True)

    base_choice_racial_mod = models.CharField(max_length=3, default='---', choices=ABILITIES_CHOICES, blank=True)

    race = models.ForeignKey(PathfinderRace, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(default='m', max_length=1, choices=(('m', 'Male'), ('f', 'Female')), blank=True)
    base_hwmod = models.IntegerField(default=0, blank=True)
    age = models.IntegerField(default=25, blank=True)
    LtoC = models.IntegerField(default=0, blank=True)
    GtoE = models.IntegerField(default=0, blank=True)
    xp_value = models.IntegerField(default=0, blank=True)
    CR = models.IntegerField(default=1, blank=True)
    speed = models.IntegerField(default=30, blank=True)

    AC = models.IntegerField(default=0, blank=True)
    touch_AC = models.IntegerField(default=0, blank=True)
    flatfooted_AC = models.IntegerField(default=0, blank=True)
    AC_details = models.TextField(max_length=1024, default='', blank=True)

    AC_armor_bonus = models.IntegerField(default=0, blank=True)
    AC_shield_bonus = models.IntegerField(default=0, blank=True)
    AC_size_modifier = models.IntegerField(default=0, blank=True)
    AC_natural_armor = models.IntegerField(default=0, blank=True)
    AC_deflection_modifier = models.IntegerField(default=0, blank=True)
    AC_misc_modifier = models.IntegerField(default=0, blank=True)

    init = models.IntegerField(default=0, blank=True)
    senses = models.TextField(default='', max_length=128, blank=True)

    total_skill_points = models.IntegerField(default=0, blank=True)

    hp = models.IntegerField(default=0, blank=True)
    hp_formula = models.TextField(max_length=1024, default='', blank=True)

    fort = models.IntegerField(default=0, blank=True)
    ref = models.IntegerField(default=0, blank=True)
    will = models.IntegerField(default=0, blank=True)
    saves_details = models.TextField(max_length=1024, default='', blank=True)

    BAB = models.IntegerField(default=0, blank=True)
    CMB = models.IntegerField(default=0, blank=True)
    CMD = models.IntegerField(default=0, blank=True)

    during_combat_tactics = models.TextField(max_length=1024, default='', blank=True)
    morale_tactics = models.TextField(max_length=1024, default='', blank=True)

    presentation = models.TextField(max_length=1024, default='', blank=True)

    base_height = models.IntegerField(default=0, blank=True)
    base_weight = models.IntegerField(default=0, blank=True)

    @property
    def alignment(self):
        LtoC = 'LNC'
        GtoE = 'GNE'
        str = f'{LtoC[self.LtoC + 1]}{GtoE[self.GtoE + 1]}'
        if str == 'NN':
            str = 'N'
        return str

    # def bonus(self, ability):
    #     import math
    #     return math.floor((ability - 10) / 2)

    def make_abilities(self):
        from collector.utils.pathfinder_tools import choose_ability,get_modifier
        if self.race.CHOICE_racial_mod == 0:
            self.STR = self.base_STR + self.race.STR_racial_mod
            self.DEX = self.base_DEX + self.race.DEX_racial_mod
            self.CON = self.base_CON + self.race.CON_racial_mod
            self.INT = self.base_INT + self.race.INT_racial_mod
            self.WIS = self.base_WIS + self.race.WIS_racial_mod
            self.CHA = self.base_CHA + self.race.CHA_racial_mod
        else:
            self.STR = self.base_STR
            self.DEX = self.base_DEX
            self.CON = self.base_CON
            self.INT = self.base_INT
            self.WIS = self.base_WIS
            self.CHA = self.base_CHA
            if self.base_choice_racial_mod == '---':
                s = choose_ability()
            else:
                s = self.base_choice_racial_mod
            v = getattr(self, f'{s}')
            setattr(self, f'{s}', v + self.race.CHOICE_racial_mod)
        self.init = get_modifier(self.DEX)

    def make_hp(self):
        from collector.utils.pathfinder_tools import dice, get_modifier
        hp_formula = []
        total_level = 0
        self.hp = 0
        for level in self.pathfinderlevel_set.all():
            die = level.character_class.hit_die
            print(die)
            hp_formula.append(f'{level.level}d{die}')
            if self.base_hp == 0:
                self.hp += dice(level.level, die)
            if level.is_favorite:
                if not level.is_giving_skill_points:
                    self.hp += level.level
                    hp_formula.append(f'{level.level}')
            total_level += level.level
        self.hp += total_level * get_modifier(self.CON) + self.base_hp
        hp_formula.append(f'{total_level * get_modifier(self.CON)}')
        str = " + ".join(hp_formula)
        print(str)
        str = str.replace("+ -", "- ")
        print(str)
        self.hp_formula = str

    def make_ac(self):
        from collector.utils.pathfinder_tools import get_modifier
        SIZE_MODIFIER = {
            'fine': 8,
            'diminutive': 4,
            'tiny': 2,
            'small': 1,
            'medium': 0,
            'large': -1,
            'huge': -2,
            'gargantuan': -4,
            'colossal': -8,
        }
        self.AC_size_modifier = SIZE_MODIFIER[self.race.size.lower()]
        self.AC = 10 + self.AC_armor_bonus + self.AC_shield_bonus + get_modifier(
            self.DEX) + self.AC_size_modifier + self.AC_natural_armor + self.AC_deflection_modifier + self.AC_misc_modifier
        self.touch_AC = 10 + self.AC_shield_bonus + get_modifier(
            self.DEX) + self.AC_size_modifier + self.AC_deflection_modifier
        self.flatfooted_AC = 10 + self.AC_armor_bonus + self.AC_size_modifier + self.AC_natural_armor
        self.fort = get_modifier(self.CON)
        self.ref = get_modifier(self.DEX)
        self.will = get_modifier(self.WIS)
        for level in self.pathfinderlevel_set.all():
            self.fort += level.fortitude_bonus()
            self.ref += level.reflex_bonus()
            self.will += level.willpower_bonus()

    def make_ranks(self):
        for rank in self.pathfinderrank_set.all():
            rank.class_skill_as = None
            highest_level = 0
            for level in self.pathfinderlevel_set.order_by('-level'):
                pathfinder_class = level.character_class
                class_skills_list = pathfinder_class.class_skills.split(', ')
                if rank.skill.name in class_skills_list:
                    if level.level > highest_level:
                        highest_level = level.level
                        rank.class_skill_as = level
                        rank.max = level.level

    def make_misc(self):
        from collector.utils.pathfinder_core import table7_3
        self.base_height, self.base_weight = table7_3(self.get_gender_display().lower(), self.race.name.lower(),
                                                      self.base_hwmod)
        self.speed = self.race.speed

    def fix_offense(self):
        from collector.utils.pathfinder_tools import get_modifier
        bestbab = 0
        for level in self.pathfinderlevel_set.all():
            bestbab += level.base_attack_bonus
        print("monk",bestbab)
        self.BAB = bestbab
        CMB_SIZE_MODIFIER = {
            'fine': -8,
            'diminutive': -4,
            'tiny': -2,
            'small': -1,
            'medium': 0,
            'large': 1,
            'huge': 2,
            'gargantuan': 4,
            'colossal': 8,
        }
        CMB_size_modifier = CMB_SIZE_MODIFIER[self.race.size.lower()]
        self.CMB = self.BAB + get_modifier(self.STR) + CMB_size_modifier
        self.CMD = self.CMB + get_modifier(self.DEX) + 10 + self.AC_misc_modifier

    def fix(self):
        super().fix()
        if self.need_fix:
            # self.race.propagate(self)
            self.fix_offense()
            self.make_misc()
            self.make_abilities()
            self.make_hp()
            self.make_ac()

            self.make_ranks()
            self.need_fix = False

    @property
    def roster(self):
        import math
        str = ""
        str += f"<div class='roster' id='roster_{self.rid}'>"
        str += f"<div class='name'><div class='lefty'>{self.name.upper()}</div><div class='righty'>CR {self.CR}</div></div>"
        if self.player:
            str += f"aka <i>{self.player.title()}</i>"
        else:
            str += f"XP {self.xp_value}"
        str += f"<br/>{self.get_gender_display().title()} {self.race.name.lower()}"
        cls = []
        bestbab = 0
        for level in self.pathfinderlevel_set.all():
            if level.base_attack_bonus > bestbab:
                bestbab = level.base_attack_bonus
            cls.append(level.class_level)
        cls_str = "/".join(cls)
        str += " " + cls_str
        str += f"<br/>{self.alignment.upper()} {self.race.size.title()} {self.race} ({math.floor(self.base_height / 12)} ft. {self.base_height - math.floor(self.base_height / 12) * 12}in. / {self.base_weight} lbs)"
        str += f"<br/><b>Init</b> {as_modifier(self.init)}; <b>Senses</b> {self.senses}"

        str += f"<div class='block'>Defense</div>"
        str += f"<b>AC</b> {self.AC}, touch {self.touch_AC}, flat-footed {self.flatfooted_AC} ({self.AC_details})"
        str += f"<br/><b>hp</b> {self.hp} ({self.hp_formula})"
        str += f"<br/><b>Fort</b> {as_modifier(self.fort)} <b>Ref</b> {as_modifier(self.ref)} <b>Will</b> {as_modifier(self.will)}; {self.saves_details}"

        str += f"<div class='block'>Offense</div>"
        str += f"<b>Speed</b> {self.speed} ft"
        str += f"<br/><b>Melee</b>  "
        str += f"<br/><b>Ranged</b>  "
        str += f"<br/><b>Special Attacks</b> "

        # str += f"<div class='block'>Tactics</div>"
        # str += f"<b>During Combat</b> {self.during_combat_tactics}"
        # str += f"<br/><b>Morale</b> {self.morale_tactics}"

        str += f"<div class='block'>Statistics</div>"
        str += f"<b>Str</b> {self.STR}, <b>Dex</b> {self.DEX}, <b>Con</b> {self.CON}, <b>Int</b> {self.INT}, <b>Wis</b> {self.WIS}, <b>Cha</b> {self.CHA} "
        str += f"<br/><b>Base Atk</b> {as_modifier(self.BAB)}; <b>CMB</b> {as_modifier(self.CMB)}; <b>CMD</b> {self.CMD}"
        str += "<br/><b>Feats </b>"
        str += "<br/><b>Skills</b> "
        skills = []
        for rank in self.pathfinderrank_set.order_by('skill'):
            skills.append(f"{rank.skill.name} {rank.rank}")
        str += ", ".join(skills) + "."
        str += "<br/><b>Languages </b>"
        str += "<br/><b>SQ </b>"
        str += "<br/><b>Gear </b>"

        from collector.models.pathfinder_weapon import PathfinderWeapon
        from collector.models.pathfinder_armor import PathfinderArmor
        for equipment in self.pathfinderequipment_set.all():
            note = ''

            if equipment.gear.is_armor:
                note = "armor"
            if equipment.gear.is_weapon:
                note = "weapon"
            str += f"<br>{equipment.gear} {note}"

        str += f"<div class='text'>{self.base_height * 2.54} / {self.base_weight / 2} <br/>{self.presentation}</div>"
        str += "</div>"
        return str


def roll_standard_abilities(modeladmin, request, queryset):
    from collector.utils.pathfinder_tools import standard_method
    for c in queryset:
        c.base_STR = standard_method()
        c.base_DEX = standard_method()
        c.base_CON = standard_method()
        c.base_INT = standard_method()
        c.base_WIS = standard_method()
        c.base_CHA = standard_method()
        c.need_fix = True
        c.save()
    short_description = 'Roll Abilities (Standard)'


def roll_classic_abilities(modeladmin, request, queryset):
    from collector.utils.pathfinder_tools import classic_method
    for c in queryset:
        c.base_STR = classic_method()
        c.base_DEX = classic_method()
        c.base_CON = classic_method()
        c.base_INT = classic_method()
        c.base_WIS = classic_method()
        c.base_CHA = classic_method()
        c.need_fix = True
        c.save()
    short_description = 'Roll Abilities (Classic)'


def refix(modeladmin, request, queryset):
    from collector.utils.pathfinder_tools import classic_method
    for c in queryset:
        c.need_fix = True
        c.save()
    short_description = 'Refix'


class PathfinderCharacterAdmin(admin.ModelAdmin):
    from collector.models.pathfinder_level import PathfinderLevelInline
    from collector.models.pathfinder_rank import PathfinderRankInline
    from collector.models.pathfinder_equipment import PathfinderEquipmentInline
    list_display = ['name', 'player', 'hp', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    actions = [roll_standard_abilities, roll_classic_abilities, refix]
    inlines = [PathfinderLevelInline, PathfinderRankInline, PathfinderEquipmentInline]
