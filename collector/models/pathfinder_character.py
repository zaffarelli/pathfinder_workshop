from django.db import models
from collector.models.character import Character
from collector.utils.pathfinder_tools import as_modifier, ABILITIES_CHOICES, get_modifier
from collector.models.pathfinder_race import PathfinderRace
from collector.models.pathfinder_feat import PathfinderFeat
from django.contrib import admin
import math


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

    volatile_STR = models.IntegerField(default=0, blank=True, null=True)
    volatile_DEX = models.IntegerField(default=0, blank=True, null=True)
    volatile_CON = models.IntegerField(default=0, blank=True, null=True)
    volatile_INT = models.IntegerField(default=0, blank=True, null=True)
    volatile_WIS = models.IntegerField(default=0, blank=True, null=True)
    volatile_CHA = models.IntegerField(default=0, blank=True, null=True)
    volatile_hp = models.IntegerField(default=0, blank=True)
    volatile_choice_racial_mod = models.CharField(max_length=3, default='---', choices=ABILITIES_CHOICES, blank=True)
    volatile_hwmod = models.IntegerField(default=0, blank=True)
    volatile_money = models.IntegerField(default=0, blank=True)
    volatile_age = models.IntegerField(default=0, blank=True)

    race = models.ForeignKey(PathfinderRace, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(default='m', max_length=1, choices=(('m', 'Male'), ('f', 'Female')), blank=True)

    age = models.IntegerField(default=0, blank=True)
    LtoC = models.IntegerField(default=0, blank=True)
    GtoE = models.IntegerField(default=0, blank=True)
    xp_value = models.IntegerField(default=0, blank=True)
    CR = models.IntegerField(default=1, blank=True)
    speed = models.IntegerField(default=30, blank=True)
    current_xp = models.PositiveIntegerField(default=0, blank=True)
    homeland = models.TextField(max_length=128, default='', blank=True)

    # feats = models.ManyToManyField(PathfinderFeat)

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

    tcl = models.IntegerField(default=0, blank=True)

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

    height = models.IntegerField(default=0, blank=True)
    weight = models.IntegerField(default=0, blank=True)

    ranked_skills = models.TextField(default="", max_length=1024, blank=True)

    dm_notes = models.TextField(default='', max_length=2048, blank=True)

    @property
    def alignment(self):
        LtoC = 'LNC'
        GtoE = 'GNE'
        str = f'{LtoC[self.LtoC + 1]}{GtoE[self.GtoE + 1]}'
        if str == 'NN':
            str = 'N'
        return str

    def make_abilities(self):
        from collector.utils.pathfinder_tools import choose_ability, get_modifier
        if self.race.CHOICE_racial_mod == 0:
            self.STR = self.volatile_STR + self.race.STR_racial_mod
            self.DEX = self.volatile_DEX + self.race.DEX_racial_mod
            self.CON = self.volatile_CON + self.race.CON_racial_mod
            self.INT = self.volatile_INT + self.race.INT_racial_mod
            self.WIS = self.volatile_WIS + self.race.WIS_racial_mod
            self.CHA = self.volatile_CHA + self.race.CHA_racial_mod
        else:
            self.STR = self.volatile_STR
            self.DEX = self.volatile_DEX
            self.CON = self.volatile_CON
            self.INT = self.volatile_INT
            self.WIS = self.volatile_WIS
            self.CHA = self.volatile_CHA
            if self.volatile_choice_racial_mod == '---':
                s = choose_ability()
            else:
                s = self.volatile_choice_racial_mod
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
            hp_formula.append(f'{level.level}d{die}')
            if self.volatile_hp == 0:
                self.hp += dice(level.level, die)
            if level.is_favorite:
                if level.favored_hit_points:
                    self.hp += level.favored_hit_points
                    hp_formula.append(f'{level.favored_hit_points}')
            total_level += level.level
        self.hp += total_level * get_modifier(self.CON) + self.volatile_hp
        hp_formula.append(f'{total_level * get_modifier(self.CON)}')
        str = " + ".join(hp_formula)
        str = str.replace("+ -", "- ")
        self.hp_formula = str

    def make_ac(self):
        from collector.utils.pathfinder_tools import get_modifier, AC_SIZE_MODIFIER
        self.AC_size_modifier = AC_SIZE_MODIFIER[self.race.size.lower()]

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
        from collector.models.pathfinder_skill import PathfinderSkill
        from collector.models.pathfinder_rank import PathfinderRank

        # Create ranks for missing skills
        ranked_skills_list = []
        for rank in self.pathfinderrank_set.all():
            if rank.rank == 0:
                rank.delete()
        for rank in self.pathfinderrank_set.all():
            ranked_skills_list.append(f'{rank.skill.name}{rank.if_wildcard}')
        for skill in PathfinderSkill.objects.order_by('name'):
            if skill.name not in ranked_skills_list:
                rank = PathfinderRank()
                rank.rank = 0
                rank.skill = skill
                rank.character = self
                rank.ability_modifier = get_modifier(getattr(self, skill.ability))
                rank.save()
        racial_modifiers = self.race.racial_modifiers.split(";")
        for rank in self.pathfinderrank_set.all():
            rank.class_skill_as = None
            highest_level = 0
            rank.class_skill_bonus = 0
            for level in self.pathfinderlevel_set.order_by('level'):
                pathfinder_class = level.character_class
                class_skills_list = pathfinder_class.class_skills.lower().split(', ')
                if rank.skill.name.lower() in class_skills_list:
                    # ranked_skills_list.append(f'{rank.skill.name}{rank.if_wildcard}')
                    if level.level > highest_level:
                        print(rank.skill.name, "is class skill for ", level)
                        highest_level = level.level
                        rank.class_skill_as = level
                        rank.max = level.level
                        print(rank.skill.name, rank.skill.ability, getattr(self, rank.skill.ability))
                        rank.ability_modifier = get_modifier(getattr(self, rank.skill.ability))
                    rank.class_skill_bonus = 3
            rank.racial_modifier = 0
            for item in racial_modifiers:
                words = item.split("=")
                if words[0] == rank.skill.name:
                    rank.racial_modifier += int(words[1])
            rank.fix()
            rank.save()
        self.ranked_skills = ", ".join(ranked_skills_list)

    def make_misc(self):
        from collector.utils.pathfinder_core import table7_3, table7_1
        self.height, self.weight = table7_3(self.get_gender_display().lower(), self.race.name.lower(),
                                            self.volatile_hwmod)
        self.speed = self.race.speed
        a,b,c = table7_1(self.race.name.lower(), self.pathfinderlevel_set.filter(is_favorite=True).first().character_class.name.lower())
        print(a,b,c)
        self.age = a + self.volatile_age

    def fix_offense(self):
        from collector.utils.pathfinder_tools import get_modifier
        bestbab = 0
        for level in self.pathfinderlevel_set.all():
            bestbab += level.base_attack_bonus
        print("monk", bestbab)
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

    def fix_defense(self):
        armors = []
        self.AC_armor_bonus = 0
        for a in self.equipped_armors():
            armors.append(f'{as_modifier(a["armor"].AC_bonus)} {a["gear"].name.lower()}')
            self.AC_armor_bonus += a["armor"].AC_bonus
        self.AC_details = ",  ".join(armors)
        self.make_ac()

    def update_tcl(self):
        self.tcl = 0
        for level in self.pathfinderlevel_set.all():
            self.tcl += level.level
        self.CR = self.tcl + 1

    def fix_statistics(self):
        pass

    def fix_spells(self):
        pass

    def fix_gear(self):
        pass

    def fix(self):
        super().fix()
        self.update_tcl()
        if self.need_fix:
            # self.race.propagate(self)
            self.fix_offense()
            self.fix_defense()
            self.fix_statistics()
            self.fix_spells()
            self.fix_gear()
            self.make_misc()
            self.make_abilities()
            self.make_hp()

            self.make_ranks()
            self.need_fix = False

    def equipped_weapons(self):
        from collector.models.pathfinder_weapon import PathfinderWeapon
        equipped_weapons = []
        for equipment in self.pathfinderequipment_set.all():
            if equipment.gear.is_weapon:
                x = equipment.gear.as_weapon
                equipped_weapons.append({'gear': equipment.gear, 'weapon': x})
        return equipped_weapons

    def equipped_armors(self, equipped=True):
        from collector.models.pathfinder_armor import PathfinderArmor
        equipped_armors = []
        if equipped:
            current_set = self.pathfinderequipment_set.filter(equipped=True)
        else:
            current_set = self.pathfinderequipment_set.all()
        for equipment in current_set:
            if equipment.gear.is_armor:
                x = equipment.gear.as_armor
                if not x.is_shield:
                    equipped_armors.append({'gear': equipment.gear, 'armor': x})
        return equipped_armors

    def equipped_shields(self, equipped=True):
        from collector.models.pathfinder_armor import PathfinderArmor
        equipped_armors = []
        if equipped:
            current_set = self.pathfinderequipment_set.filter(equipped=True)
        else:
            current_set = self.pathfinderequipment_set.all()
        for equipment in current_set:
            if equipment.gear.is_armor:
                x = equipment.gear.as_armor
                if x.is_shield:
                    equipped_armors.append({'gear': equipment.gear, 'armor': x})
        return equipped_armors

    @property
    def is_small(self):
        if "Small Size" in self.race.special_abilities.all().values_list('name', flat=True):
            return True
        return False

    @property
    def total_feats(self):
        x = math.floor((self.tcl + 1) / 2)
        return x

    @property
    def character_class_levels(self):
        ccl = []
        for level in self.pathfinderlevel_set.all():
            ccl.append(level.class_level.lower())
        return " ".join(ccl)

    @property
    def roster(self):
        from collector.utils.pathfinder_tools import get_modifier, as_modifier
        str = ""
        str += f"<div class='roster hidden' id='roster__{self.rid}'>"
        display_special = ''
        if self.player:
            display_special = "player"
            if self.player == 'Dungeonmaster NPC':
                display_special = "dm_npc"
        str += f"<div class='name {display_special}'><div class='lefty'>{self.name.upper()}</div><div class='righty'>CR {self.CR}</div></div>"
        if self.player:
            str += f"aka <i>{self.player}</i>"
        else:
            str += f"XP {self.xp_value}"
        str += f"<br/>{self.get_gender_display().title()} {self.race.name.lower()}"
        cls = []
        bestbab = 0
        for level in self.pathfinderlevel_set.all():
            if level.base_attack_bonus > bestbab:
                bestbab = level.base_attack_bonus
            cls.append(level.class_level.lower())
        cls_str = "/".join(cls)
        str += " " + cls_str
        str += f"<br/>{self.alignment.upper()} {self.race.size.title()} {self.race} ({math.floor(self.height / 12)} ft. {self.height - math.floor(self.height / 12) * 12}in. / {self.weight} lbs)"
        str += f"<br/><b>Init</b> {as_modifier(self.init)}"
        if self.race.senses:
            str += f"; <b>Senses</b> {self.race.senses}"

        str += f"<div class='block'>Defense</div>"
        str += f"<b>AC</b> {self.AC}, touch {self.touch_AC}, flat-footed {self.flatfooted_AC} ({self.AC_details})"
        str += f"<br/><b>hp</b> {self.hp} ({self.hp_formula})"
        str += f"<br/><b>Fort</b> {as_modifier(self.fort)} <b>Ref</b> {as_modifier(self.ref)} <b>Will</b> {as_modifier(self.will)}; {self.saves_details}"

        str += f"<div class='block'>Offense</div>"
        str += f"<b>Speed</b> {self.speed} ft"
        weapons_contact = []
        weapons_ranged = []
        for x in self.equipped_weapons():
            sized_dmg = x['weapon'].DMG_medium
            if self.is_small:
                sized_dmg = x['weapon'].DMG_small
            attack_bonus = x["weapon"].attack_bonus + self.BAB + get_modifier(self.STR)
            dmg_bonus = x["weapon"].DMG_bonus + get_modifier(self.STR)
            if x['weapon'].range > 0:
                attack_bonus = x["weapon"].attack_bonus + self.BAB + get_modifier(self.DEX)
                dmg_bonus = x["weapon"].DMG_bonus + get_modifier(self.STR)
                weapon_str = f"{x['gear'].name} {as_modifier(attack_bonus)} ({sized_dmg}{as_modifier(dmg_bonus)}/{x['weapon'].critical})"
                weapons_ranged.append(weapon_str)
            else:
                weapon_str = f"{x['gear'].name} {as_modifier(attack_bonus)} ({sized_dmg}{as_modifier(dmg_bonus)}/{x['weapon'].critical})"
                weapons_contact.append(weapon_str)
        str += f"<br/><b>Melee</b> {', '.join(weapons_contact)}"
        str += f"<br/><b>Ranged</b> {', '.join(weapons_ranged)}"
        str += f"<br/><b>Special Attacks</b> "

        # str += f"<div class='block'>Tactics</div>"
        # str += f"<b>During Combat</b> {self.during_combat_tactics}"
        # str += f"<br/><b>Morale</b> {self.morale_tactics}"

        str += f"<div class='block'>Statistics</div>"
        str += f"<b>Str</b> {self.STR}, <b>Dex</b> {self.DEX}, <b>Con</b> {self.CON}, <b>Int</b> {self.INT}, <b>Wis</b> {self.WIS}, <b>Cha</b> {self.CHA} "
        str += f"<br/><b>Base Atk</b> {as_modifier(self.BAB)}; <b>CMB</b> {as_modifier(self.CMB)}; <b>CMD</b> {self.CMD}"
        str += f"<br/><b>Feats</b> {self.roster_feats}"
        str += "<br/><b>Skills</b> "
        # skills = []
        # for rank in self.pathfinderrank_set.order_by('skill'):
        #     skills.append(f"{rank.skill.name} {rank.rank}")
        str += self.roster_skills + "."
        str += f"<br/><b>Languages </b> {self.roster_languages}"
        str += "<br/><b>SQ </b>"
        str += f"<div class='block'>Spells</div>"
        str += f"{self.roster_spells}"
        str += f"<div class='block'>Gear</div>"
        stuff = []
        for equipment in self.pathfinderequipment_set.all():
            note = ''
            if equipment.gear.is_armor:
                note = "(armor)"
            if equipment.gear.is_weapon:
                note = "(weapon)"
            stuff.append(f"{equipment.gear} {note}")
        str += f"{', '.join(stuff)}."
        str += f"<div class='block'>Notes</div>"
        str += f"<b>XP</b> {self.current_xp}"
        str += f"<div class='text'>{self.height * 2.54} / {self.weight / 2} <br/>Total feats: {self.total_feats}<br/>{self.presentation}</div>"
        str += "</div>"
        return str

    @property
    def roster_languages(self):
        list = []
        languages = self.race.languages.split(";")
        for language in languages:
            list.append(language)
        for level in self.pathfinderlevel_set.all():
            if level.character_class.languages:
                languages = level.character_class.languages.split(";")
                for language in languages:
                    list.append(language)
        return ", ".join(list) + "."

    @property
    def roster_spells(self):
        from collector.models.pathfinder_spell import PathfinderSpell
        list = []
        languages = self.race.languages.split(";")
        for level in self.pathfinderlevel_set.all():
            if level.character_class.is_spellcasting_class:
                cl, ms, cc = level.character_class.current_caster_level(level.level)
                spell_level = -1
                if cl:
                    # Todo: set dynamic filter here
                    list.append(f'<i>{cl.label}</i><ul>')
                    for spell in PathfinderSpell.objects.filter(source="PFRPG Core", druid__lte=level.level).order_by(
                            'druid', 'name'):
                        if spell_level != spell.SLA_Level:
                            if spell_level != -1:
                                list.append(", ".join(level_list))
                                list.append(f".</li>")
                            level_list = []
                            spell_level = spell.SLA_Level
                            list.append(f"<li><em>Level {spell.SLA_Level}:</em> ")
                        level_list.append(f"{spell.name}")
                    list.append(", ".join(level_list))
                    list.append(f".</li>")
                    list.append(f'</ul>')
        return "".join(list) + "."

    @property
    def roster_feats(self):
        list = []
        for feat in self.pathfindercharacterfeat_set.all():
            label = f"{feat.feat.name}"
            if feat.feat.is_fighter_feat:
                label += f"<i class='fa-solid fa-asterisk fa-2xs'></i>"
            if feat.choice:
                label += f" ({feat.choice})"
            list.append(label)
        return ", ".join(list) + "."

    @property
    def roster_skills(self):
        from collector.models.pathfinder_skill import PathfinderSkill
        list = []
        for rank in self.pathfinderrank_set.order_by('skill'):
            avoid = False
            cs_flagstart = ""
            cs_flagend = ""
            if rank.rank > 0:
                cs_flagstart = "<i>"
                cs_flagend = "</i>"
            else:
                if rank.skill.is_trained_only:
                    avoid = True
            if not avoid:
                if rank.skill.is_wildcard:
                    if rank.rank > 0:
                        list.append(
                            f"{cs_flagstart}{rank.skill.name}{rank.if_wildcard}{cs_flagend}&nbsp;{as_modifier(rank.total_score)}")
                else:
                    list.append(
                        f"{cs_flagstart}{rank.skill.name}{cs_flagend}&nbsp;{as_modifier(rank.total_score)}{rank.details}")
        return ", ".join(list)

    @property
    def sheet_skills(self):
        from collector.models.pathfinder_skill import PathfinderSkill
        list = []
        for rank in self.pathfinderrank_set.order_by('skill'):
            list.append(rank.to_json())
        return list


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
    from collector.models.pathfinder_character_feat import PathfinderCharacterFeatInline
    ordering = ['-player', '-tcl']
    list_display = ['name', 'player', 'tcl', 'hp', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA', 'dm_notes']
    actions = [roll_standard_abilities, roll_classic_abilities, refix]
    inlines = [PathfinderLevelInline, PathfinderRankInline, PathfinderEquipmentInline, PathfinderCharacterFeatInline]
